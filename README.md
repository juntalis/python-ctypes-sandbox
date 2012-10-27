## Python CTypes Playground

This repository is more of a less sandbox for experimenting with various Win32-based functionality using Python CTypes. Most of it will most likely deal with the internals of the Portable Executable File Format, but some of it may revolve around some more basic stuff. At the moment, there a few things some might find interesting or useful. I've detailed these below. All code found in this repository (except peutils) is released under WTFPL, so do whatever you want with it - I don't care.

#### Python Remote CTypes (RDLL) - rdll.py

*** 32-bit Python Only at the moment ***

This module contains a few ctypes DLL interfaces for injecting dlls into remote processes, and calling functions in them as if they were regular DLLs. To avoid having to load the DLL into the local python process, it currently uses the [http://code.google.com/p/pefile/](PEFile module) to parse the DLL exports table. I'm debating rewriting this part, but we'll just have to see. The only negligible different I can currently think of between this API and the API found in the regular Python DLL interfaces is the DLL constructor, and that you HAVE TO specify the argtypes/restypes using this module.

**Examples**

	# The example below injects "testdll.dll" into the python process's parent process,
	# then calls Initialize and Finalize. Both functions execute in the context of the parent
	# process.
	testdll = RCDLL('testdll.dll')
	Initialize = testdll.Initialize
	Initialize.restype = None
	Initialize.argtypes = []
	Initialize()
	testdll.Finalize()

	# Does the same as above, but injects into the process with the current process ID of 5004
	testdll = RCDLL('testdll.dll', pid=5004)
	Initialize = testdll.Initialize
	Initialize.restype = None
	Initialize.argtypes = []
	Initialize()
	testdll.Finalize()


#### Python DLL Injection - inject.py

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