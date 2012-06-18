from ctypes import *

from ctypes.wintypes import WCHAR
from ctypes.wintypes import LONG
from ctypes.wintypes import HANDLE
from ctypes.wintypes import LPVOID
from ctypes.wintypes import LPCVOID
from ctypes.wintypes import BOOL
from ctypes.wintypes import WORD
from ctypes.wintypes import DWORD
from ctypes.wintypes import LPCSTR
from ctypes.wintypes import LPSTR
from ctypes.wintypes import HINSTANCE
from ctypes.wintypes import HMODULE
_stdcall_libraries = {}
_stdcall_libraries['kernel32.dll'] = WinDLL('kernel32.dll')


CHAR = c_char
ULONG_PTR = c_ulong
SIZE_T = ULONG_PTR
LPDWORD = POINTER(DWORD)
FARPROC = CFUNCTYPE(None)
class tagPROCESSENTRY32(Structure):
	_fields_ = [
		('dwSize', DWORD),
		('cntUsage', DWORD),
		('th32ProcessID', DWORD),
		('th32DefaultHeapID', ULONG_PTR),
		('th32ModuleID', DWORD),
		('cntThreads', DWORD),
		('th32ParentProcessID', DWORD),
		('pcPriClassBase', LONG),
		('dwFlags', DWORD),
		('szExeFile', CHAR * 260),
	]
PROCESSENTRY32 = tagPROCESSENTRY32
PPROCESSENTRY32 = POINTER(tagPROCESSENTRY32)
LPPROCESSENTRY32 = POINTER(tagPROCESSENTRY32)
class tagTHREADENTRY32(Structure):
	pass
tagTHREADENTRY32._fields_ = [
	('dwSize', DWORD),
	('cntUsage', DWORD),
	('th32ThreadID', DWORD),
	('th32OwnerProcessID', DWORD),
	('tpBasePri', LONG),
	('tpDeltaPri', LONG),
	('dwFlags', DWORD),
]
LPTHREADENTRY32 = POINTER(tagTHREADENTRY32)
THREADENTRY32 = tagTHREADENTRY32
PTHREADENTRY32 = POINTER(tagTHREADENTRY32)
class _PROCESS_INFORMATION(Structure):
	pass
_PROCESS_INFORMATION._fields_ = [
	('hProcess', HANDLE),
	('hThread', HANDLE),
	('dwProcessId', DWORD),
	('dwThreadId', DWORD),
]
LPPROCESS_INFORMATION = POINTER(_PROCESS_INFORMATION)
PROCESS_INFORMATION = _PROCESS_INFORMATION
class _SECURITY_ATTRIBUTES(Structure):
	pass
_SECURITY_ATTRIBUTES._fields_ = [
	('nLength', DWORD),
	('lpSecurityDescriptor', LPVOID),
	('bInheritHandle', BOOL),
]
LPSECURITY_ATTRIBUTES = POINTER(_SECURITY_ATTRIBUTES)
LPTHREAD_START_ROUTINE = WINFUNCTYPE(DWORD, LPVOID)
WriteProcessMemory = _stdcall_libraries['kernel32.dll'].WriteProcessMemory
WriteProcessMemory.restype = BOOL
WriteProcessMemory.argtypes = [HANDLE, LPVOID, LPCVOID, SIZE_T, POINTER(SIZE_T)]
WriteProcessMemory.__doc__ = \
"""BOOL WriteProcessMemory(HANDLE hProcess, LPVOID lpBaseAddress, LPCVOID lpBuffer, SIZE_T nSize, SIZE_T * lpNumberOfBytesWritten)
ppython.h:86"""
VirtualAllocEx = _stdcall_libraries['kernel32.dll'].VirtualAllocEx
VirtualAllocEx.restype = LPVOID
VirtualAllocEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD, DWORD]
VirtualAllocEx.__doc__ = \
"""LPVOID VirtualAllocEx(HANDLE hProcess, LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect)
ppython.h:87"""
VirtualFreeEx = _stdcall_libraries['kernel32.dll'].VirtualFreeEx
VirtualFreeEx.restype = BOOL
VirtualFreeEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD]
VirtualFreeEx.__doc__ = \
"""BOOL VirtualFreeEx(HANDLE hProcess, LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType)
ppython.h:88"""
LoadLibraryA = _stdcall_libraries['kernel32.dll'].LoadLibraryA
LoadLibraryA.restype = HMODULE
LoadLibraryA.argtypes = [LPCSTR]
LoadLibraryA.__doc__ = \
"""HMODULE LoadLibraryA(LPCSTR lpLibFileName)
ppython.h:89"""
GetProcAddress = _stdcall_libraries['kernel32.dll'].GetProcAddress
GetProcAddress.restype = FARPROC
GetProcAddress.argtypes = [HMODULE, LPCSTR]
GetProcAddress.__doc__ = \
"""FARPROC GetProcAddress(HMODULE hModule, LPCSTR lpProcName)
ppython.h:90"""
Process32First = _stdcall_libraries['kernel32.dll'].Process32First
Process32First.restype = BOOL
Process32First.argtypes = [HANDLE, LPPROCESSENTRY32]
Process32First.__doc__ = \
"""BOOL Process32First(HANDLE hSnapshot, LPPROCESSENTRY32 lppe)
ppython.h:91"""
Process32Next = _stdcall_libraries['kernel32.dll'].Process32Next
Process32Next.restype = BOOL
Process32Next.argtypes = [HANDLE, LPPROCESSENTRY32]
Process32Next.__doc__ = \
"""BOOL Process32Next(HANDLE hSnapshot, LPPROCESSENTRY32 lppe)
ppython.h:91"""
Thread32First = _stdcall_libraries['kernel32.dll'].Thread32First
Thread32First.restype = BOOL
Thread32First.argtypes = [HANDLE, LPTHREADENTRY32]
Thread32First.__doc__ = \
"""BOOL Thread32First(HANDLE hSnapshot, LPTHREADENTRY32 lpte)
ppython.h:93"""
Thread32Next = _stdcall_libraries['kernel32.dll'].Thread32Next
Thread32Next.restype = BOOL
Thread32Next.argtypes = [HANDLE, LPTHREADENTRY32]
Thread32Next.__doc__ = \
"""BOOL Thread32Next(HANDLE hSnapshot, LPTHREADENTRY32 lpte)
ppython.h:93"""
GetCurrentProcessId = _stdcall_libraries['kernel32.dll'].GetCurrentProcessId
GetCurrentProcessId.restype = DWORD
GetCurrentProcessId.argtypes = []
GetCurrentProcessId.__doc__ = \
"""DWORD GetCurrentProcessId()
ppython.h:94"""
CreateToolhelp32Snapshot = _stdcall_libraries['kernel32.dll'].CreateToolhelp32Snapshot
CreateToolhelp32Snapshot.restype = HANDLE
CreateToolhelp32Snapshot.argtypes = [DWORD, DWORD]
CreateToolhelp32Snapshot.__doc__ = \
"""HANDLE CreateToolhelp32Snapshot(DWORD dwFlags, DWORD th32ProcessID)
ppython.h:95"""
OpenProcess = _stdcall_libraries['kernel32.dll'].OpenProcess
OpenProcess.restype = HANDLE
OpenProcess.argtypes = [DWORD, BOOL, DWORD]
OpenProcess.__doc__ = \
"""HANDLE OpenProcess(DWORD dwDesiredAccess, BOOL bInheritHandle, DWORD dwProcessId)
ppython.h:96"""
CreateRemoteThread = _stdcall_libraries['kernel32.dll'].CreateRemoteThread
CreateRemoteThread.restype = HANDLE
CreateRemoteThread.argtypes = [HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD]
CreateRemoteThread.__doc__ = \
"""HANDLE CreateRemoteThread(HANDLE hProcess, LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, DWORD dwCreationFlags, LPDWORD lpThreadId)
ppython.h:97"""
WaitForSingleObject = _stdcall_libraries['kernel32.dll'].WaitForSingleObject
WaitForSingleObject.restype = DWORD
WaitForSingleObject.argtypes = [HANDLE, DWORD]
WaitForSingleObject.__doc__ = \
"""DWORD WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds)
ppython.h:98"""
FreeLibrary = _stdcall_libraries['kernel32.dll'].FreeLibrary
FreeLibrary.restype = BOOL
FreeLibrary.argtypes = [HMODULE]
FreeLibrary.__doc__ = \
"""BOOL FreeLibrary(HMODULE hLibModule)
ppython.h:99"""
CloseHandle = _stdcall_libraries['kernel32.dll'].CloseHandle
CloseHandle.restype = BOOL
CloseHandle.argtypes = [HANDLE]
CloseHandle.__doc__ = \
"""BOOL CloseHandle(HANDLE hObject)
ppython.h:100"""


"""#define TH32CS_SNAPPROCESS 0x00000002"""
TH32CS_SNAPPROCESS = 0x00000002

"""#define TH32CS_SNAPTHREAD 0x00000004"""
TH32CS_SNAPTHREAD = 0x00000004

"""#define PROC_THREAD_SNAPSHOT (TH32CS_SNAPPROCESS|TH32CS_SNAPTHREAD)"""
PROC_THREAD_SNAPSHOT = 0x00000006

"""#define MEM_COMMIT 0x1000"""
MEM_COMMIT = 0x1000

"""#define MEM_RELEASE 0x8000"""
MEM_RELEASE = 0x8000

"""#define PAGE_READWRITE 0x04"""
PAGE_READWRITE = 0x04

"""#define PROCESS_QUERY_INFORMATION 0x0400"""
PROCESS_QUERY_INFORMATION = 0x0400

"""#define PROCESS_CREATE_THREAD 0x0002"""
PROCESS_CREATE_THREAD = 0x0002

"""#define PROCESS_VM_OPERATION 0x0008"""
PROCESS_VM_OPERATION = 0x0008

"""#define PROCESS_VM_WRITE 0x0020"""
PROCESS_VM_WRITE = 0x0020

"""#define PROCESS_MOST (PROCESS_QUERY_INFORMATION | PROCESS_CREATE_THREAD | PROCESS_VM_OPERATION | PROCESS_VM_WRITE) """
PROCESS_MOST = 0x042A

"""#define INFINITE 0xFFFFFFFF"""
INFINITE = -1

FALSE = 0
TRUE = 1
NULL = 0

__all__ = ['FALSE','TRUE','NULL','FARPROC', 'CreateToolhelp32Snapshot', 'LPPROCESSENTRY32',
		'WriteProcessMemory', 'VirtualAllocEx',
		'tagPROCESSENTRY32', 'WaitForSingleObject', 'CHAR',
		'LoadLibraryA', 'LPTHREAD_START_ROUTINE', 'ULONG_PTR',
		'CreateRemoteThread', 'LPPROCESS_INFORMATION',
		'_SECURITY_ATTRIBUTES', 'tagTHREADENTRY32',
		'VirtualFreeEx', 'THREADENTRY32', 'PROCESS_INFORMATION','Process32Next', 
		'Process32First', 'LPSECURITY_ATTRIBUTES', 'OpenProcess', 'Thread32Next',
		'GetProcAddress', 'LPTHREADENTRY32', 'GetCurrentProcessId',
		'PPROCESSENTRY32', 'Thread32First', 'FreeLibrary',
		'PROCESSENTRY32', 'LPDWORD', 'SIZE_T', 'PTHREADENTRY32',
		'_PROCESS_INFORMATION', 'CloseHandle', 'TH32CS_SNAPPROCESS',
		'TH32CS_SNAPTHREAD', 'PROC_THREAD_SNAPSHOT', 'MEM_COMMIT', 'MEM_RELEASE',
		'PAGE_READWRITE','PROCESS_QUERY_INFORMATION', 'PROCESS_CREATE_THREAD',
		'PROCESS_VM_OPERATION', 'PROCESS_VM_WRITE','PROCESS_MOST', 'INFINITE']


