# coding: utf-8
"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.

Non-portable stuff.
"""
import code, sys, os, time
mydir = os.path.abspath(os.path.dirname(__file__))
if mydir.lower() not in [p.lower() for p in sys.path]:
	sys.path.insert(0, mydir)

from _kernel32 import *
import extern.pefile as pefile

pe = pefile.PE(GetModuleFileName(NULL), fast_load=True)
_imgbase = pe.OPTIONAL_HEADER.ImageBase
_modbase = GetModuleHandle()
mem_offset = lambda a: a + _modbase - _imgbase

def address_of(cobj):
	"""
	Ctypes variation of this function doesn't appear to be
	accurate all the time, thus I decided to write my own.
	"""
	return cast(cobj, c_void_p).value


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

class node_arg(Structure):
	_fields_ = [
		('unknown', c_ubyte * 60),
		('cmdline', c_wchar_p),
	]

jump_entry_func = WINFUNCTYPE(c_int, POINTER(node_arg))

class jump_entry(Structure):
	_fields_ = [
		('_name', ULONG_PTR),
		('func', jump_entry_func),
		('flags', WORD),
		('msgno', ULONG),
		('msgno2', ULONG),
		('msgno3', ULONG),
	]

	@property
	def funcaddr(self):
		return address_of(self.func)

	@property
	def name(self):
		if long(self._name) == 0L:
			return None
		else:
			return wstring_at(self._name).encode()

	@property
	def uname(self):
		if long(self._name) == 0L:
			return None
		else:
			return wstring_at(self._name).encode().upper()

	@name.setter
	def name(self, value):
		if isinstance(value, basestring):
			cvalue = create_unicode_buffer(value, len(value))
			self._name = address_of(cvalue)
		else:
			self._name = value

class FuncConsole(code.InteractiveConsole):
	pass

class JumpTable(object):
	_entries_ = {}
	def __init__(self, base):
		self._addr = mem_offset(base)
		# Trying to figure out a good portable way
		# to find the end of our jump table and
		# start of our prompt buffer.
		self._end = mem_offset(0x4AD25E40)

	def explore(self, idx):
		global stub, funcsh
		funcsh.set_idx(idx)
		self[idx].func = stub

	def __getitembyname__(self, name):
		i = 0
		while True:
			try:
				entry = self.__getitem__(i)
				if entry.uname == name:
					super(JumpTable, self).__setattr__(name, entry)
					return entry
				i += 1
			except IndexError:
				raise AttributeError(name)

	def __getitem__(self, name_or_idx):
		if isinstance(name_or_idx, basestring):
			result = self.__getitembyname__(name_or_idx.upper())
		elif type(name_or_idx) in [ long, int]:
			name_or_idx = int(name_or_idx)
			if name_or_idx in self._entries_:
				result = jump_entry.from_address(self._entries_[name_or_idx]['addr'])
			else:
				addr = self._addr + (sizeof(jump_entry) * name_or_idx)
				if addr >= self._end:
					errmsg = 'Index %d is out of range of the jump table!' % name_or_idx
					raise IndexError(errmsg)
				result = jump_entry.from_address(addr)
				self._entries_[name_or_idx] = {
					'addr': addr,
					'name': result.uname
				}
		else:
			raise IndexError('Dont know what to do with index specified.')
		return result


class ComSpec(object):
	def __init__(self):
		self._funcs_ = _funcs
		self.echo_flag = InternalData(0x4AD2408C, restype=BOOL)
		# Table of internal functions that expect a parse node as their one
		# and only argument. Unfortunately, I haven't figured out much about
		# the struct of the parse node, other than the fact that it has a
		# wchar* offset 60 bytes from its
		self.jump_table = JumpTable(0x4AD25880)
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
class FuncConsole(code.InteractiveConsole):
	def __init__(self, table):
		self.table = table
		locs = locals()
		globs = globals()
		for k in globs.keys():
			if k not in locs:
				locs[k] = globs[k]
		for k in shell.locals.keys():
			if k not in locs:
				locs[k] = shell.locals[k]
		self.__name__ = 'unknown'
		self.original = None
		code.InteractiveConsole.__init__(self, locs, "<console>")
	
	def set_idx(self, idx):
		entry = self.table[idx]
		if entry.name is None:
			self.__name__ = '(Interactive Console in Jump Entry #%d)' % idx
		else:
			self.__name__ = '(Interactive Console in Jump Entry %s)' % entry.name
		self.original = jump_entry_func.from_address(entry.funcaddr)
		return self
		
	def chain_interact(self):
		try:
			self.interact(self.__name__)
		except KeyboardInterrupt:
			pass
		return self

funcsh = FuncConsole(cmd.jump_table)
def entry_func_stub(node):
	global funcsh
	return funcsh.chain_interact().original(node)
stub = jump_entry_func(entry_func_stub)
funcsh.locals = locals()
#cmd.jump_table.explore(0)
shell.locals = locals()
try:
	shell.interact('(Interactive Console in Command Prompt)')
except KeyboardInterrupt:
	pass

