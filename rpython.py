#/usr/bin/env python
# coding: utf-8
"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.
"""
import os, sys, pytab
from rdll import *
from ctypes import util
from _kernel32 import is_x64

if __name__ == '__main__':
	if is_x64():
		print 'This script requires an 32-bit version of Python.\n'
		print 'If you have a 32-bit version of Python, but dont want to have to add it to your PATH, add a bat file to your PATH called, "x86env.bat" or "x86env.cmd" that temporarily adds it to your PATH.\n'
		print 'Something like:'
		print '@set PATH=%%PATH:\\mypythonx64folder\\=\\mypythonx86folder\\%%\n'
		sys.exit(1)
	python = RCDLL(handle=sys.dllhandle)
	smsvcrt = util.find_library(util.find_msvcrt())
	if smsvcrt is None:
		smsvcrt = util.find_library('msvcr100')
	msvcrt = RCDLL(smsvcrt)
	rkernel32 = RWinDLL(util.find_library('kernel32'))

	pyhome = os.path.dirname(sys.executable)
	pypath = ';'.join(sys.path)

	path = 'PATH=%s' % (pyhome + ';' + os.environ['PATH']).replace(';;',';')
	putenv = msvcrt._putenv
	putenv.argtypes = [ c_char_p ]
	putenv.restype = c_int
	putenv(path)
	putenv('PYTHONPATH=%s' % pypath)

	pytab.populate_exports(python)
	python.Py_SetProgramName(sys.executable)
	#python.Py_SetPythonHome(pyhome)
	python.Py_Initialize()

	python.Py_GetPath()
	main = python.PyImport_AddModule("__main__")
	PyRun_SimpleString = python.PyRun_SimpleString
	PyRun_SimpleString.argtypes = [ c_char_p ]
	PyRun_SimpleString.restype = c_int
	PyRun_SimpleString("from comspec import *")
	python.Py_Finalize()
	rkernel32.FreeLibrary(python._handle)