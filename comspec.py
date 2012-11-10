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

_proc_base = GetModuleHandleA(cast(NULL, c_char_p))
_re_base = 0x4AD00000
_offset = lambda a: a - _re_base + _proc_base

class InternalFunc(object):

	def __init__(self, offset, restype, *argtypes):
		self.restype = restype
		self.argtypes = argtypes if len(argtypes) > 0 else []
		self.addr = _offset(offset)
		self._func = WINFUNCTYPE(self.restype, *self.argtypes)(self.addr)

	def __call__(self, *args, **kwargs):
		return self._func(*args)

# Currently mapped internal functions.
_funcs = {
	'dir': InternalFunc(0x4AD0AEEB, BOOL, c_wchar_p),
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

class ComSpec(object):
	def __init__(self):
		self._funcs_ = _funcs
		self.echo_flag = cast(_offset(0x4AD2408C), POINTER(BOOL))
		# This is actually the jump table for some of the internal functions, but whatever. Haven't
		# figured a way to implement this in ctypes.
		self.jump_table = cast(_offset(0x4AD25880), c_wchar_p)

	def __getattr__(self, item):
		if self._funcs_.has_key(item):
			return self.__getitem__(item)
		else:
			return super(ComSpec, self).__getattribute__(item)

	def __getitem__(self, item):
		if self._funcs_.has_key(item):
			return self._funcs_[item]
		elif type(item) in [ int, long, c_long, c_int8, c_int16, c_int32, c_int64]:
			return cast(_offset(item), c_void_p)
		else:
			#noinspection PyUnresolvedReferences
			return super(ComSpec, self).__getitem__(item)

cmd = ComSpec()
code.interact('(Interactive Console in Command Prompt)', None, locals())