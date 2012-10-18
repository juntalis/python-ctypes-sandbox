#/usr/bin/env python
from _kernel32 import *

_platform = __import__('platform')
_isx64 = _platform.architecture()[0] == '64bit'
del _platform

def is_x64(): return _isx64

def create_remote_thread(hProcess, func, args = None):
	# For the return of our call.
	valResult = DWORD(0)

	# Allocate some memory in the remote process
	if args is not None:
		pszArg = alloc_set_var(hProcess, args)
		if pszArg is None:
			CloseHandle(hProcess)
			raise WinError('Failed to allocate and set our dll string')
	else:
		pszArg = NULL

	hRemoteThread = CreateRemoteThread(
		hProcess, NULL_SECURITY_ATTRIBUTES, 0,
		func, pszArg, 0L, byref(c_ulong(0L))
	)
	if hRemoteThread == NULL:
		if args is not None:
			VirtualFreeEx(hProcess, pszArg, 0, MEM_RELEASE)
		CloseHandle(hProcess)
		raise WinError('Failed to start our remote thread.')

	WaitForSingleObject(hRemoteThread, INFINITE)
	GetExitCodeThread(hRemoteThread, byref(valResult))
	CloseHandle(hRemoteThread)
	if args is not None: VirtualFreeEx(hProcess, pszArg, 0, MEM_RELEASE)
	return valResult


def get_func_offset(dll, funcName):
	pFunc = GetProcAddress(dll, funcName)
	if pFunc == NULL:
		raise WinError('Failed to get the address of function: %s' % funcName)
	pFunc = cast(pFunc, c_void_p)
	return pFunc.value - dll.value


def alloc_set_var(hProcess, val):
	"""
	BOOL alloc_set_varA(LPCSTR* buffer, HANDLE hProcess, LPCSTR val)
	{
		SIZE_T buflen = (lstrlen(val) + 1) * sizeof(const char);
		if (!(*buffer = (LPCSTR) VirtualAllocEx(hProcess, NULL, buflen, MEM_COMMIT, PAGE_READWRITE)))
			return_error("Could not allocate memory for our test call.");

		if (!WriteProcessMemory(hProcess, (LPVOID)*buffer, (LPCVOID)val, (SIZE_T)buflen, NULL))
			return_error("Could write to our remote variable..");
		return TRUE;
	}
	"""
	if type(val) == str:
		val = create_string_buffer(val)
	buflen = sizeof(val)

	buffer = VirtualAllocEx(hProcess, 0L, buflen, MEM_COMMIT, PAGE_READWRITE)
	if buffer == NULL:
		raise Exception('Could not allocate our remote buffer.')

	if WriteProcessMemory(hProcess, buffer, cast(val, LPCVOID), buflen, byref(c_ulong(0L))) == FALSE:
		raise Exception('Could not write to our remote variable.')

	return buffer


def find_parent_process():
	"""
	Obtain the process and thread identifiers of the parent process.

	BOOL get_parent_process( LPPROCESS_INFORMATION ppi )
	{
		HANDLE hSnap;
		PROCESSENTRY32 pe;
		THREADENTRY32	te;
		DWORD	id = GetCurrentProcessId();
		BOOL	 fOk;

		hSnap = CreateToolhelp32Snapshot( TH32CS_SNAPPROCESS|TH32CS_SNAPTHREAD, id );

		if (hSnap == INVALID_HANDLE_VALUE)
			return FALSE;

		find_proc_id( hSnap, id, &pe );
		if (!find_proc_id( hSnap, pe.th32ParentProcessID, &pe ))
		{
			CloseHandle( hSnap );
			return FALSE;
		}

		te.dwSize = sizeof(te);
		for (fOk = Thread32First( hSnap, &te ); fOk; fOk = Thread32Next( hSnap, &te ))
			if (te.th32OwnerProcessID == pe.th32ProcessID)
				break;

		CloseHandle( hSnap );

		ppi->dwProcessId = pe.th32ProcessID;
		ppi->dwThreadId	= te.th32ThreadID;

		return fOk;
	}
	"""
	pid = GetCurrentProcessId()

	hSnap = CreateToolhelp32Snapshot( PROC_THREAD_SNAPSHOT, 0 )
	if hSnap == NULL:
		raise WinError('Could not create a Toolhelp32Snapshot')

	(fOk,pe) = find_proc_id(hSnap, pid)
	if fOk == FALSE:
		raise WinError('Could not find current proc')

	ppid = pe.th32ParentProcessID
	fOk,ppe = find_proc_id(hSnap, ppid)
	if fOk == FALSE:
		raise WinError('Could not find parent proc id')

	te = THREADENTRY32()
	te.dwSize = SZTHREADENTRY
	fOk = Thread32First(hSnap, byref(te))
	while fOk != FALSE:
		if te.th32OwnerProcessID == ppe.th32ProcessID: break
		fOk = Thread32Next(hSnap, byref(te))
	if fOk == FALSE:
		raise WinError('Could not find thread.')
	CloseHandle(hSnap)
	return ppe.th32ProcessID, te.th32ThreadID


def find_proc_id(hSnap, pid):
	"""
	Search each process in the snapshot for id.
	BOOL find_proc_id( HANDLE snap, DWORD id, LPPROCESSENTRY32 ppe )
	{
		BOOL fOk;
		ppe->dwSize = sizeof(PROCESSENTRY32);
		for (fOk = Process32First( snap, ppe ); fOk; fOk = Process32Next( snap, ppe ))
			if (ppe->th32ProcessID == id)
				break;
		return fOk;
	}
	"""
	ppe = PROCESSENTRY32()
	ppe.dwSize = SZPROCESSENTRY
	fOk = Process32First(hSnap, byref(ppe))
	while fOk != FALSE:
		if ppe.th32ProcessID == pid: break
		fOk = Process32Next(hSnap, byref(ppe))
	return fOk, ppe