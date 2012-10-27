#/usr/bin/env python
import os, sys, pytab
from rdll import *
from ctypes import util

if __name__ == '__main__':
	python = RCDLL(handle=sys.dllhandle)
	msvcrt = RCDLL(util.find_library(util.find_msvcrt()))
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
	PyRun_SimpleString("import code")
	PyRun_SimpleString("code.interact(None, None, locals())")