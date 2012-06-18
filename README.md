#### Python DLL Injection

This example uses the Python ctypes module to inject the included dll, testdll.dll into the parent process. (Most likely cmd.exe if you run this example from the command prompt)

Currently, this example only works on x86 processes and with the 32-bit version of Python. (I'm guessing this is due to the size difference in datatypes needed for calling the appropriate win32 functions) I'll see if I can get a working example for x64 processes when I get a chance.

From the command prompt:

	C:\Development\cpp.sandbox\ppython\ppython>build.bat
	Setting environment for using Microsoft Visual Studio 2010 x86 tools.
	Microsoft (R) 32-bit C/C++ Optimizing Compiler Version 16.00.40219.01 for 80x86
	Copyright (C) Microsoft Corporation.  All rights reserved.

	testdll.c
	Microsoft (R) Incremental Linker Version 10.00.40219.01
	Copyright (C) Microsoft Corporation.  All rights reserved.

	/out:testdll.exe
	-DLL
	-OPT:REF
	-OPT:ICF
	-OUT:testdll.dll
	-IMPLIB:C:\Development\cpp.sandbox\ppython\ppython\obj\testdll.lib
	C:\Development\cpp.sandbox\ppython\ppython\obj\testdll.obj
	
	C:\Development\cpp.sandbox\ppython\ppython>python inject.py
	python.exe
	cmd.exe
	PARENT: Hello World
	PARENT: Goodbye World
	All done!