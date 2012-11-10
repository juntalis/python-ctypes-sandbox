## Python CTypes Playground

This repository is more of a less sandbox for experimenting with various Win32-based functionality using Python CTypes. Most of it will most likely deal with the internals of the Portable Executable File Format, but some of it may revolve around some more basic stuff. At the moment, there a few things some might find interesting or useful. I've detailed these below. All code found in this repository - except peutils, and code found in the pyctypes file (See the comments of that file for author information) - is released under WTFPL, so do whatever you want with it - I don't care.

For a simpler example of using python to inject DLLs, see older versions of this repository. The original example was broken due to my lack of foresight.

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


#### Command Prompt Reversing

Running the rpy.cmd file will run a script that injects the current python DLL into your command prompt, initializes the interpreter, and opens a python shell in that process with some pre-existing work I'm doing on reverse engineering command prompt. (Work I'm doing as I debate whether or not to go through with a project idea)

Unfortunately, the current code is most likely not all that portable across different versions of command prompt, but if you do happen to have the same version as mine, you should be able to call various of the built-in command prompt functions such as:

	cmd.start('/WAIT calc.exe')
	cmd.set('')
	cmd.dir('..')

If you run the rpython.py file from an existing command prompt, calling cmd.prompt() will print the current value of your PROMPT. In addition to the builtin functions I mapped, there's a few internally-used functions that I'm working on reversing.