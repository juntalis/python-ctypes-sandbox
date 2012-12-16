# coding: utf-8
"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.

Non-portable stuff.
"""
import code
from _kernel32 import *
import extern.pefile as pefile

pe = pefile.PE(GetModuleFileName(NULL), fast_load=True)
_imgbase = pe.OPTIONAL_HEADER.ImageBase
_modbase = GetModuleHandle()
mem_offset = lambda a: a + _modbase - _imgbase

class InternalFunc(object):

	def __init__(self, offset, restype, *argtypes):
		self.restype = restype
		self.argtypes = argtypes if len(argtypes) > 0 else []
		self.addr = mem_offset(offset)
		self._func = WINFUNCTYPE(self.restype, *self.argtypes)(self.addr)

	def __call__(self, *args, **kwargs):
		return self._func(*args)

def InternalData(offset, restype = None, size = None):
	addr = mem_offset(offset)
	retfunc = string_at
	if restype == c_wchar_p:
		retfunc = wstring_at
	elif restype is not None:
		if size is None:
			retfunc = lambda a: restype.from_address(a)
		else:
			# We'll assume this should be an array
			retfunc = lambda a,s: (restype * s).from_address(a)
	
	if size is None:
		return retfunc(addr)
	else:
		return retfunc(addr, size)

# Currently mapped internal functions.
_funcs = {
	'chdir': InternalFunc(0x4AD10511, c_int, c_wchar_p),
	'dir': InternalFunc(0x4AD0AEEB, c_int, c_wchar_p),
	'prompt': InternalFunc(0x4AD0C60C, None),
	'dumpstr': InternalFunc(0x4AD1F174, c_int),
	'set': InternalFunc(0x4AD1C9D2, c_int, c_wchar_p),
	'start': InternalFunc(0x4AD08EC3, c_int, c_wchar_p),
	'dispatch': InternalFunc(0x4AD01492, c_int, c_int, DWORD), # First arg deals with redirection.
	'getfuncptr': InternalFunc(0x4A974177, DWORD, c_int),
	'findcmd': InternalFunc(0x4AD040F2, c_int, DWORD, c_wchar_p, c_wchar_p),
}

# From what I've gathered, cmd.findcmd returns a value representing the index of
# a particular command in the jump table. The constants below are the indexes for
# various commands.
CMD_DIR = 0
CMD_DEL = 1
CMD_TYPE = 3
CMD_COPY = 4
CMD_CD = 5
CMD_RENAME = 7
CMD_ECHO = 9
CMD_SET = 10
CMD_PAUSE = 11
CMD_DATE = 12
CMD_TIME = 13
CMD_PROMPT = 14
CMD_MKDIR = 16
CMD_RMDIR = 18
CMD_PATH = 19
CMD_GOTO = 20
CMD_SHIFT = 21
CMD_CLS = 22
CMD_CALL = 23
CMD_VERIFY = 24
CMD_VER = 25
CMD_VOL = 26
CMD_EXIT = 27
CMD_SETLOCAL = 28
CMD_ENDLOCAL = 29
CMD_CHCP = 30
CMD_START = 31
CMD_APPEND = 32
CMD_KEYS = 33
CMD_MOVE = 34
CMD_PUSHD = 35
CMD_POPD = 36
CMD_BREAK = 37
CMD_ASSOC = 38
CMD_FTYPE = 39
CMD_COLOR = 40
CMD_FOR = 41
CMD_IF = 42
CMD_REM = 43

class envdata(Structure):
	_fields_ = [
		('data', c_wchar_p),
		('size', c_uint),
		('max', c_uint),
	]

class jump_entry(Structure):
	_fields_ = [
		('name', c_wchar_p),
		('func', WINFUNCTYPE(c_int)),
		('flags', WORD),
		('msgno', ULONG),
		('msgno2', ULONG),
		('msgno3', ULONG)
	]

class ComSpec(object):
	def __init__(self):
		self._funcs_ = _funcs
		self.echo_flag = InternalData(0x4AD2408C, restype=BOOL)
		# Table of internal functions that expect a parse node as their one
		# and only argument. Unfortunately, I haven't figured out much about
		# the struct of the parse node, other than the fact that it has a
		# wchar* offset 60 bytes from its
		self.jump_table = InternalData(0x4AD25880, restype=jump_entry)
		self.cd = self.chdir

	def __getattr__(self, item):
		if self._funcs_.has_key(item):
			return self.__getitem__(item)
		else:
			return super(ComSpec, self).__getattribute__(item)

	def __getitem__(self, item):
		if self._funcs_.has_key(item):
			return self._funcs_[item]
		elif type(item) in [ int, long, c_long, c_int8, c_int16, c_int32, c_int64]:
			return cast(mem_offset(item), c_void_p)
		else:
			#noinspection PyUnresolvedReferences
			return super(ComSpec, self).__getitem__(item)

cmd = ComSpec()
shell = code.InteractiveConsole(locals())
shell.interact('(Interactive Console in Command Prompt)')
