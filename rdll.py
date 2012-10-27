#!/usr/bin/env python
# encoding: utf-8
"""
rdll.py
Created by Charles on 10/25/12.

		This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.
"""
import os
from _ctypes import FUNCFLAG_CDECL as _FUNCFLAG_CDECL,\
FUNCFLAG_PYTHONAPI as _FUNCFLAG_PYTHONAPI,\
FUNCFLAG_USE_ERRNO as _FUNCFLAG_USE_ERRNO,\
FUNCFLAG_USE_LASTERROR as _FUNCFLAG_USE_LASTERROR
from _kernel32 import PLoadLibraryW as PLoadLibrary
from extern import pefile

__all__ = []

import functools
from _kernel32 import *

_platform = __import__('platform')
_isx64 = _platform.architecture()[0] == '64bit'
del _platform

def is_x64(): return _isx64

# Utility stuff (decorators/base classes/functions)
def memoize(obj):
	"""
	From the Python Decorator Library:
	Cache the results of a function call with specific arguments. Note that this decorator ignores **kwargs.
	"""
	cache = obj.cache = {}

	@functools.wraps(obj)
	def memoizer(*args, **kwargs):
		if args not in cache:
			cache[args] = obj(*args, **kwargs)
		return cache[args]

	return memoizer


def _find_parent_process():
	"""
	Obtain the process and thread identifiers of the parent process.

	BOOL get_parent_process( LPPROCESS_INFORMATION ppi )
	{
		HANDLE hSnap;
		PROCESSENTRY32 pe;
		THREADENTRY32	te;
		DWORD	id = GetCurrentProcessId();
		BOOL	 fOk;

		hSnap = CreateToolhelp32Snapshot( TH32CS_SNAPPROCESS|TH32CS_SNAPTHREAD, id );

		if (hSnap == INVALID_HANDLE_VALUE)
			return FALSE;

		find_proc_id( hSnap, id, &pe );
		if (!find_proc_id( hSnap, pe.th32ParentProcessID, &pe ))
		{
			CloseHandle( hSnap );
			return FALSE;
		}

		te.dwSize = sizeof(te);
		for (fOk = Thread32First( hSnap, &te ); fOk; fOk = Thread32Next( hSnap, &te ))
			if (te.th32OwnerProcessID == pe.th32ProcessID)
				break;

		CloseHandle( hSnap );

		ppi->dwProcessId = pe.th32ProcessID;
		ppi->dwThreadId	= te.th32ThreadID;

		return fOk;
	}
	"""
	pid = GetCurrentProcessId()

	hSnap = CreateToolhelp32Snapshot(PROC_THREAD_SNAPSHOT, 0)
	if hSnap == NULL:
		raise WinError('Could not create a Toolhelp32Snapshot')

	(fOk, pe) = _find_proc_id(hSnap, pid)
	if fOk == FALSE:
		raise WinError('Could not find current proc')

	ppid = pe.th32ParentProcessID
	fOk, ppe = _find_proc_id(hSnap, ppid)
	if fOk == FALSE:
		raise WinError('Could not find parent proc id')

	te = THREADENTRY32()
	te.dwSize = SZTHREADENTRY
	fOk = Thread32First(hSnap, byref(te))
	while fOk != FALSE:
		if te.th32OwnerProcessID == ppe.th32ProcessID: break
		fOk = Thread32Next(hSnap, byref(te))
	if fOk == FALSE:
		raise WinError('Could not find thread.')
	CloseHandle(hSnap)
	return ppe.th32ProcessID, te.th32ThreadID


def _find_proc_id(hSnap, pid):
	"""
	Search each process in the snapshot for id.
	BOOL find_proc_id( HANDLE snap, DWORD id, LPPROCESSENTRY32 ppe )
	{
		BOOL fOk;
		ppe->dwSize = sizeof(PROCESSENTRY32);
		for (fOk = Process32First( snap, ppe ); fOk; fOk = Process32Next( snap, ppe ))
			if (ppe->th32ProcessID == id)
				break;
		return fOk;
	}
	"""
	ppe = PROCESSENTRY32()
	ppe.dwSize = SZPROCESSENTRY
	fOk = Process32First(hSnap, byref(ppe))
	while fOk != FALSE:
		if ppe.th32ProcessID == pid: break
		fOk = Process32Next(hSnap, byref(ppe))
	return fOk, ppe


def _bypid(pid):
	"""
	Find a process and it's main thread by its process ID.
	"""
	hSnap = CreateToolhelp32Snapshot(PROC_THREAD_SNAPSHOT, 0)
	if hSnap == NULL: raise WinError('Could not create a Toolhelp32Snapshot')
	(fOk, pe) = _find_proc_id(hSnap, pid)
	if fOk == FALSE: raise WinError('Could not find process by id: %d' % pid)

	# Find the thread
	te = THREADENTRY32()
	te.dwSize = SZTHREADENTRY
	fOk = Thread32First(hSnap, byref(te))
	while fOk != FALSE:
		if te.th32OwnerProcessID == pe.th32ProcessID: break
		fOk = Thread32Next(hSnap, byref(te))
	if fOk == FALSE: raise WinError('Could not find thread.')
	CloseHandle(hSnap)
	return pe.th32ProcessID, te.th32ThreadID


def _pack_args(*args):
	class _Args(Structure): pass

	fields = []
	for i, arg in enumerate(args):
		fields.append(('arg%d' % i, type(arg),))
	_Args._fields_ = fields
	return _Args(*args)


class _RCFuncPtr(object):
	_addr_ = 0
	_flags_ = None
	_restype_ = None
	_funcptr_ = None
	_hprocess_ = None

	def _valueof(self, arg):
		if not hasattr(arg, '_type_'):
			return arg
		elif hasattr(arg, 'value'):
			return arg.value
		elif hasattr(arg, 'contents'):
			return arg.contents
		else:
			raise Exception('Don\'t know how to get the value of arg.\nType: %s' % type(arg))

	def _valtoargtype(self, arg, argtype):
		result = 0
		if type(arg) in [str, unicode]:
			if argtype == c_char_p:
				result = create_string_buffer(arg, len(arg) + 1)
			elif argtype == c_wchar_p:
				result = create_unicode_buffer(arg, len(arg) + 1)
			elif argtype._type_ == c_ubyte:
				result = (c_ubyte * len(arg) + 1)()
				for i, c in enumerate(arg):
					result[i] = c
			else:
				raise Exception('Don\'t know how to convert string, "%s" into type: %s' % (arg, argtype))
		# Array type
		elif hasattr(argtype, '_length_')\
		or type(argtype._type_) != str: # Pointer type
			result = cast(arg, argtype)
		elif hasattr(argtype, 'value'):
			result = argtype(arg)
		else:
			raise Exception('Don\'t know how to convert arg to argtype.\nArg: %s\nArgtype: %s' % (arg, argtype))
		return result

	def _alloc_set_var(self, val):
		"""
		BOOL alloc_set_varA(LPCSTR* buffer, HANDLE hProcess, LPCSTR val)
		{
			SIZE_T buflen = (lstrlen(val) + 1) * sizeof(const char);
			if (!(*buffer = (LPCSTR) VirtualAllocEx(hProcess, NULL, buflen, MEM_COMMIT, PAGE_READWRITE)))
				return_error("Could not allocate memory for our test call.");

			if (!WriteProcessMemory(hProcess, (LPVOID)*buffer, (LPCVOID)val, (SIZE_T)buflen, NULL))
				return_error("Could write to our remote variable..");
			return TRUE;
		}
		"""
		buflen = sizeof(val)
		buffer = VirtualAllocEx(self._hprocess_, 0L, buflen, MEM_COMMIT, PAGE_READWRITE)
		if buffer == NULL:
			raise Exception('Could not allocate our remote buffer.')

		if WriteProcessMemory(self._hprocess_, LPCVOID(buffer), val, buflen, ULONG_PTR(0)) == FALSE:
			raise Exception('Could not write to our remote variable.')

		return buffer

	def __call__(self, *more): # real signature unknown; restored from __doc__
		""" x.__call__(...) <==> x(...) """
		funcptr = self._funcptr_
		result = DWORD(0L) if funcptr.restype is None else funcptr.restype()
		lpParameter = NULL
		if funcptr.argtypes is not None and len(funcptr.argtypes) > 0:
			args = []
			argcount = len(more)
			for i, argtype in enumerate(funcptr.argtypes):
				arg = 0
				if i > argcount:
					arg = argtype()
				elif hasattr(more[i], '_type_'):
					if more[i]._type_ == argtype:
						arg = more[i]
					else:
						arg = self._valtoargtype(self._valueof(more[i]), argtype)
				else:
					arg = self._valtoargtype(more[i])
				args.append(arg)
			if argcount > 1:
				lpParameter = _pack_args(*args)
			else:
				lpParameter = args[0]
		if hasattr(lpParameter, '_b_needsfree_') and lpParameter._b_needsfree_ == 1 and bool(lpParameter):
			lpParameter = self._alloc_set_var(lpParameter)
		hRemoteThread = CreateRemoteThread(
			self._hprocess_, NULL_SECURITY_ATTRIBUTES, 0,
			cast(self._addr_, LPTHREAD_START_ROUTINE),
			lpParameter, 0L, byref(c_ulong(0L))
		)
		if hRemoteThread == NULL:
			if hasattr(lpParameter, '_b_needsfree_') and lpParameter._b_needsfree_ == 1 and bool(lpParameter):
				VirtualFreeEx(self._hprocess_, lpParameter, 0, MEM_RELEASE)
			CloseHandle(self._hprocess_)
			raise WinError('Failed to start our remote thread.')

		WaitForSingleObject(hRemoteThread, INFINITE)
		GetExitCodeThread(hRemoteThread, cast(byref(result), LPDWORD))
		CloseHandle(hRemoteThread)
		if hasattr(lpParameter, '_b_needsfree_') and lpParameter._b_needsfree_ == 1 and bool(lpParameter):
			VirtualFreeEx(self._hprocess_, lpParameter, 0, MEM_RELEASE)
		return result


	def __init__(self, offset, funcid, rdll):
		self._addr_ = offset
		if self._flags_ == _FUNCFLAG_CDECL:
			self._funcptr_ = CFUNCTYPE(self._restype_)
		elif self._flags_ == _FUNCFLAG_STDCALL:
			self._funcptr_ = WINFUNCTYPE(self._restype_)
		elif self._flags_ == _FUNCFLAG_PYTHONAPI:
			self._funcptr_ = PYFUNCTYPE(self._restype_)
		self._funcptr_._func_flags_ = self._flags_


	def __nonzero__(self):
		""" x.__nonzero__() <==> x != 0 """
		return self._funcptr_.__nonzero__()

	def __repr__(self): # real signature unknown; restored from __doc__
		""" x.__repr__() <==> repr(x) """
		return self._funcptr_.__repr__()

	@memoize
	def _has(self, key): return key in dir(_RCFuncPtr)

	def __setattr__(self, key, value):
		if self._has(key):
			super(_RCFuncPtr, self).__setattr__(key, value)
		else:
			setattr(self._funcptr_, key, value)

	def __getattr__(self, key):
		return super(_RCFuncPtr, self).__getattr__(key) if\
		self._has(key) else\
		getattr(self._funcptr_, key)


class RCDLL(object):
	_func_flags_ = _FUNCFLAG_CDECL
	_func_restype_ = c_int
	_hprocess_ = 0
	_hthread_ = 0
	_exports_ = {}
	_funcs_ = {}

	def __init__(self, name = None, pid = 0, thid = 0, mode = DEFAULT_MODE, handle = None, use_errno = False,
				 use_last_error = False):
		if name is None and handle is None:
			raise WindowsError('We need either a name or a handle to a preloaded DLL to create a DLL interface.')
		elif name is None:
			self._name = GetModuleFileName(handle)
		else:
			self._name = name

		flags = self._func_flags_
		if use_errno:
			flags |= _FUNCFLAG_USE_ERRNO
		if use_last_error:
			flags |= _FUNCFLAG_USE_LASTERROR

		self._hthread_ = thid
		pi, ti = 0, 0
		if pid == 0:
			check = _find_parent_process()
			if check is None:
				raise WinError('Failed to open our parent process and no pid specified.')
			pi, ti = check
		else:
			pi, ti = _bypid(pid)

		if self._hthread_ == 0:
			self._hthread_ = ti
		self._hprocess_ = OpenProcess(PROCESS_MOST, FALSE, pi)

		class _FuncPtr(_RCFuncPtr):
			_flags_ = flags
			_restype_ = self._func_restype_
			_hprocess_ = self._hprocess_

		self._FuncPtr = _FuncPtr
		self._handle = self.__inject__()
		if self._handle == 0:
			raise WindowsError('Could not inject your library: %s' % self._name)

		self.__populate_exports__()

	def __inject__(self):
		val = create_unicode_buffer(self._name, len(self._name) + 1)
		buflen = sizeof(val)

		buffer = VirtualAllocEx(self._hprocess_, 0L, buflen, MEM_COMMIT, PAGE_READWRITE)
		if buffer == NULL:
			raise Exception('Could not allocate our remote buffer.')

		if WriteProcessMemory(self._hprocess_, buffer, cast(val, LPCVOID), buflen, ULONG_PTR(0)) == FALSE:
			raise Exception('Could not write to our remote variable.')

		hRemoteThread = CreateRemoteThread(
			self._hprocess_, NULL_SECURITY_ATTRIBUTES, 0,
			PLoadLibrary, buffer, 0L, byref(c_ulong(0L))
		)
		if hRemoteThread == NULL:
			VirtualFreeEx(self._hprocess_, buffer, 0, MEM_RELEASE)
			CloseHandle(self._hprocess_)
			raise WinError('Failed to start our remote thread.')
		WaitForSingleObject(hRemoteThread, INFINITE)

		result = c_ulong(0)
		GetExitCodeThread(hRemoteThread, byref(result))
		CloseHandle(hRemoteThread)
		VirtualFreeEx(self._hprocess_, buffer, 0, MEM_RELEASE)
		return result.value

	def __populate_exports__(self):
		if len(os.path.splitext(self._name)[1].lower()) == 0:
			self._name += '.dll'
		pe = pefile.PE(self._name, fast_load = True)
		direxport = pe.OPTIONAL_HEADER.DATA_DIRECTORY[0]
		exportsobj = pe.parse_export_directory(direxport.VirtualAddress, direxport.Size)
		pe.close()
		for export in exportsobj.symbols:
			self._exports_[export.name] =\
			self._exports_[export.ordinal] =\
			self._handle + export.address

	def __repr__(self):
		return "<%s '%s', handle %x at %x>" %\
			   (self.__class__.__name__, self._name,
				(self._handle & (_sys.maxint * 2 + 1)),
				id(self) & (_sys.maxint * 2 + 1))

	def __getattr__(self, name):
		if name.startswith('__') and name.endswith('__'):
			raise AttributeError(name)
		func = self.__getitem__(name)
		super(RCDLL, self).__setattr__(name, func)
		self._funcs_[name] = func
		#setattr(self, name, func)
		return func

	def __setattr__(self, key, value):
		if key in self._exports_.keys():
			self._funcs_[key] = value
		else:
			super(RCDLL, self).__setattr__(key, value)

	def __getitem__(self, name_or_ordinal):
		if name_or_ordinal in self._funcs_.keys():
			return self._funcs_[name_or_ordinal]
		ordinal = isinstance(name_or_ordinal, (int, long))
		if not self._exports_.has_key(name_or_ordinal):
			if ordinal: raise WindowsError('Could not find address of function at ordinal: %d' % name_or_ordinal)
			else: raise WindowsError('Could not find address of function named: %s' % name_or_ordinal)
		func = self._FuncPtr(self._exports_[name_or_ordinal], name_or_ordinal, self)
		if not ordinal:
			func.__name__ = name_or_ordinal
		return func

class RPyDLL(RCDLL):
	"""This class represents the Python library itself.  It allows to
		access Python API functions.  The GIL is not released, and
		Python exceptions are handled correctly.
		"""
	_func_flags_ = _FUNCFLAG_CDECL | _FUNCFLAG_PYTHONAPI

class RWinDLL(RCDLL):
	"""This class represents a dll exporting functions using the
			Windows stdcall calling convention.
			"""
	_func_flags_ = _FUNCFLAG_STDCALL

rcdll = LibraryLoader(RCDLL)
rwindll = LibraryLoader(RWinDLL)
rpydll = LibraryLoader(RPyDLL)

if __name__ == '__main__':
	testdll = RCDLL('testdll.dll')
	Initialize = testdll.Initialize
	Initialize.restype = None
	Initialize.argtypes = []
	Initialize()
	testdll.Finalize()
