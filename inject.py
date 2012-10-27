"""
This program is free software. It comes without any warranty, to
the extent permitted by applicable law. You can redistribute it
and/or modify it under the terms of the Do What The Fuck You Want
To Public License, Version 2, as published by Sam Hocevar. See
http://sam.zoy.org/wtfpl/COPYING for more details.
"""
from cutil import create_remote_thread, get_func_offset, _find_parent_process
from pyctypes import *

if __name__=='__main__':
	# Okay, given we already have the address to LoadLibrary, we can
	# begin by getting our parent process id and thread id.
	procPair = _find_parent_process()
	if procPair is None:
		raise WinError('Failed to locate our parent process.')
	(pi, ti) = procPair

	# Open our parent process for writing.
	hProcess = OpenProcess(PROCESS_MOST, FALSE, pi)
	if hProcess == NULL:
		raise WinError('Failed to open our parent process.')

	# Load the DLL locally
	pythonDLL = PythonDLL()
	if pythonDLL.handle == NULL:
		raise WinError('Failed to find our own Python DLL.. This should not happen.')
	hlMyDll = HMODULE(pythonDLL.handle)

	# Get the offsets of both functions.
	szInitOffset = get_func_offset(hlMyDll, 'Initialize')
	szFinOffset = get_func_offset(hlMyDll, 'Finalize')
	FreeLibrary(hlMyDll)

	# Get the address of our function
	prMyDll = create_remote_thread(hProcess, PLoadLibraryW, pythonDLL.name)
	hrMyDll = prMyDll.value

	# Build our functions given the addresses
	rInitialize = FARPROC(hrMyDll + szInitOffset)
	rFinalize = FARPROC(hrMyDll + szFinOffset)

	# Execute them in remote threads
	create_remote_thread(hProcess, cast(rInitialize, LPTHREAD_START_ROUTINE))
	create_remote_thread(hProcess, cast(rFinalize, LPTHREAD_START_ROUTINE))

	# Note: If we called the remote functions like this, it would actually show our python process as the result in GetModuleFileName(NULL,x,y)
	#rInitialize()
	#rFinalize()

	# Lastly, free the library in our parent process and close the handle.

	# Currently causing issues.
	#create_remote_thread(hProcess, PFreeLibrary, prMyDll)

	CloseHandle(hProcess)
	print 'All done!'