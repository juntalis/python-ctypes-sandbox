from _kernel32 import *
from ctypes import *
from ctypes.wintypes import *


"""
// Search each process in the snapshot for id.
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
def find_proc_id(hSnap, pid):
	ppe = PROCESSENTRY32()
	ppe.dwSize = sizeof(PROCESSENTRY32)
	fOk = Process32First(hSnap, byref(ppe))
	while fOk != FALSE:
		if ppe.th32ProcessID == pid:
			break
		fOk = Process32Next(hSnap, byref(ppe))
	print ppe.szExeFile
	return fOk, ppe


"""
// Obtain the process and thread identifiers of the parent process.
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
def find_parent_process():
	pid = GetCurrentProcessId()
	hSnap = CreateToolhelp32Snapshot( PROC_THREAD_SNAPSHOT, 0 )
	if hSnap == NULL:
		return None
	(fOk,pe) = find_proc_id(hSnap, pid)
	if fOk == FALSE:
		print 'Could not find current proc'
		return None
	ppid = pe.th32ParentProcessID
	fOk,ppe = find_proc_id(hSnap, ppid)
	if fOk == FALSE:
		print 'Could not find parent proc id'
		return None
	te = THREADENTRY32()
	te.dwSize = sizeof(THREADENTRY32)
	fOk = Thread32First(hSnap, byref(te))
	while fOk != FALSE:
		if (te.th32OwnerProcessID == ppe.th32ProcessID):
			break
		fOk = Thread32Next(hSnap, byref(te))
	if fOk == FALSE:
		print 'Could not find thread.'
		return None
	CloseHandle(hSnap)
	return (pe.th32ProcessID, te.th32ThreadID)

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
def alloc_set_var(hProcess, val):
	buflen = (len(val)+1) * sizeof(c_char)
	buffer = VirtualAllocEx(hProcess, 0L, buflen, MEM_COMMIT, PAGE_READWRITE)
	if buffer == NULL:
		print 'Could not allocate our remote buffer.'
		return None
	val += '\0'
	# cast(val, LPCVOID)
	if WriteProcessMemory(hProcess, buffer, val, buflen, byref(c_ulong(0L))) == FALSE:
		print 'Could not write to our remote variable.'
		return None
	
	return buffer

def main():
	# First load kernel32.dll
	kernel32 = LoadLibraryA('kernel32.dll')
	if kernel32 == NULL:
		print 'Could not load kernel32.dll'
		return
	
	# Next, get the address to our LoadLibraryA function.
	# Using the LoadLibraryA function from our _kernel32 module might do this
	# but I'm not sure sooo..
	rLoadLibraryA = GetProcAddress(kernel32, 'LoadLibraryA')
	if rLoadLibraryA == NULL:
		print 'Could not get address to our LoadLibraryA@kernel32.dll function'
		return
	
	# Get our parent process id and thread id.
	parent = find_parent_process()
	if parent is None:
		FreeLibrary(kernel32)
		return
	(pi, ti) = parent
	
	# Open our parent process for writing.
	hProcess = OpenProcess(PROCESS_MOST, FALSE, pi)
	if hProcess == NULL:
		print 'Failed to open our parent process.'
		FreeLibrary(kernel32)
		return
	
	pszMyDll = alloc_set_var(hProcess, 'testdll.dll')
	if pszMyDll is None:
		print 'Failed to allocate and set our dll string'
		CloseHandle(hProcess)
		FreeLibrary(kernel32)
		return
	
	hRemoteThreadLoadLibraryA = CreateRemoteThread( \
		hProcess, \
		cast(NULL, LPSECURITY_ATTRIBUTES), \
		0, \
		cast(rLoadLibraryA, LPTHREAD_START_ROUTINE), \
		pszMyDll, \
		0L, \
		byref(c_ulong(0L)) \
	)
	if hRemoteThreadLoadLibraryA == NULL:
		print 'Failed to start our remote thread.'
		VirtualFreeEx(hProcess, pszMyDll, 0, MEM_RELEASE)
		CloseHandle(hProcess)
		#FreeLibrary(kernel32)
		return
	
	WaitForSingleObject(hRemoteThreadLoadLibraryA, INFINITE)
	VirtualFreeEx(hProcess, pszMyDll, 0, MEM_RELEASE)
	CloseHandle(hRemoteThreadLoadLibraryA)
	CloseHandle(hProcess)
	#FreeLibrary(kernel32)
	
	print 'All done!'

main()