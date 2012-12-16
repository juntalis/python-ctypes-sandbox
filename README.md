## Python CTypes Playground

This repository is more of a less sandbox for experimenting with various Win32-based functionality using Python CTypes. Most of it will most likely deal with the internals of the Portable Executable File Format, but some of it may revolve around some more basic stuff. At the moment, there a few things some might find interesting or useful. I've detailed these below. All code found in this repository - except peutils, and code found in the pyctypes file (See the comments of that file for author information) - is released under WTFPL, so do whatever you want with it - I don't care.

For a simpler example of using python to inject DLLs, see older versions of this repository. The original example was broken due to my lack of foresight.

#### Python Remote CTypes (RDLL) - rdll.py

**32-bit Python Only at the moment**

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

Unfortunately, the current code is most likely not all that portable across different versions of command prompt. Being that this is a sandbox for exploration, I decided to simply be lazy and hard code the address offsets, rather than searching for signatures within the current memory. Still if you do happen to have the same version as mine (Using the WOW64 Command Prompt included in Windows 7 SP1 x64), you should be able to call various of the built-in command prompt functions such as:

	cmd.start('/WAIT calc.exe')
	cmd.set('')
	cmd.dir('..')

If you run the rpython.py file from an existing command prompt, calling cmd.prompt() will print the current value of your PROMPT. In addition to the builtin functions I mapped, there's a few internally-used functions that I'm working on reversing. Additionally, I've now mapped out most of the internal jump table, which can be accessed at `cmd.jump_table`.

**Note:** The `cmd.jump_table.explore(index)` function does not currently work. Because all python functions are currently created in a separate thread, trying to use them for C callbacks is not currently possible. To fix this, I'm either going to need to change the way I do the code injection in rdll.py to use the main thread context, or I'll need to set up the proper thread support in rpython.py's initialization process.

At any time, you can hit Ctrl+C to exit the interpreter and drop down into the working command prompt process. Changes made to the "name" field of the aforementioned jump table should persist, allowing for interesting (but pointless) modifications like below:

	Microsoft Windows [Version 6.1.7601]
	Copyright (c) 2009 Microsoft Corporation.  All rights reserved.
	 
	C:\Development\py.workspace\python-remote>rpy.cmd
	(Interactive Console in Command Prompt)
	>>> cmd.jump_table[0].name
	u'DIR'
	>>> newname = create_unicode_buffer('SOME_WEIRD_COMMAND')
	>>> cmd.jump_table[0].name = cast(newname, c_wchar_p)
	>>> ^C
	 
	C:\Development\py.workspace\python-remote>dir
	'dir' is not recognized as an internal or external command,
	operable program or batch file.
	 
	C:\Development\py.workspace\python-remote>some_weird_command
	 Volume in drive C is Windows 7 x64
	 Volume Serial Number is XXXX-XXXX
	 
	 Directory of C:\Development\py.workspace\python-remote
	 
	12/15/2012  08:16 PM    <DIR>          .
	12/15/2012  08:16 PM    <DIR>          ..
	11/10/2012  07:39 PM                99 .gitignore
	12/15/2012  08:11 PM             4,150 comspec.py
	12/15/2012  08:16 PM             5,852 comspec.pyc
	11/10/2012  12:54 PM    <DIR>          extern
	11/29/2012  02:45 PM             2,222 pyctypes.py
	11/10/2012  12:36 PM           258,842 pytab.py
	11/29/2012  02:46 PM            17,616 rdll.py
	11/10/2012  12:57 PM             2,993 README.md
	12/15/2012  08:15 PM               504 rpy.cmd
	12/15/2012  08:16 PM             2,083 rpython.py
	12/15/2012  07:38 PM            13,994 _kernel32.py
	12/15/2012  07:49 PM            12,114 _kernel32.pyc
				  14 File(s)        324,475 bytes
				   7 Dir(s)  445,443,272,704 bytes free
	 
	C:\Development\py.workspace\python-remote>

