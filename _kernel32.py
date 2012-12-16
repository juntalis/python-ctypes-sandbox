from ctypes import *
from ctypes.wintypes import *
import _ctypes, sys


#############
# Constants #
#############

kernel32 = WinDLL('kernel32.dll')
is_x64 = sizeof(c_void_p) == sizeof(c_ulonglong)
is_pypy = hasattr(sys, 'pypy_version_info')


# ToolhelpSnapshot flags
TH32CS_SNAPPROCESS = 0x00000002
TH32CS_SNAPTHREAD = 0x00000004
PROC_THREAD_SNAPSHOT = 0x00000006

# OpenProcess flags
MEM_COMMIT = 0x1000
MEM_RELEASE = 0x8000
PAGE_READWRITE = 0x04
PROCESS_QUERY_INFORMATION = 0x0400
PROCESS_CREATE_THREAD = 0x0002
PROCESS_VM_OPERATION = 0x0008
PROCESS_VM_WRITE = 0x0020
PROCESS_MOST = 0x042A

# Generic constants
INFINITE = -1
FALSE = 0
TRUE = 1
NULL = 0

#########
# Types #
#########

# Simple type declarations
CHAR = c_char
LPDWORD = POINTER(DWORD)
FARPROC = CFUNCTYPE(None)
LPFARPROC = POINTER(FARPROC)
LPTHREAD_START_ROUTINE = WINFUNCTYPE(DWORD, LPVOID)

# Some general type declarations
PWORD = POINTER(WORD)
PDWORD = POINTER(DWORD)
PHMODULE = POINTER(HMODULE)
LONG_PTR = c_longlong if is_x64 else LONG
ULONG_PTR = c_ulonglong if is_x64 else DWORD
UINT_PTR = c_ulonglong if is_x64 else c_uint
SIZE_T = ULONG_PTR
POINTER_TYPE = ULONG_PTR
LP_POINTER_TYPE = POINTER(POINTER_TYPE)

c_uchar_p = POINTER(c_ubyte)
c_ushort_p = POINTER(c_ushort)

# Struct/Union declarations
class PROCESSENTRY32(Structure):
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

class THREADENTRY32(Structure):
	_fields_ = [
		('dwSize', DWORD),
		('cntUsage', DWORD),
		('th32ThreadID', DWORD),
		('th32OwnerProcessID', DWORD),
		('tpBasePri', LONG),
		('tpDeltaPri', LONG),
		('dwFlags', DWORD),
	]

class PROCESS_INFORMATION(Structure):
	_fields_ = [
		('hProcess', HANDLE),
		('hThread', HANDLE),
		('dwProcessId', DWORD),
		('dwThreadId', DWORD),
	]

class SECURITY_ATTRIBUTES(Structure):
	_fields_ = [
		('nLength', DWORD),
		('lpSecurityDescriptor', LPVOID),
		('bInheritHandle', BOOL),
	]

class MODULEINFO(Structure):
	_fields = [
		('lpBaseOfDll', LPVOID),
		('SizeOfImage', DWORD),
		('EntryPoint', LPVOID),
	]

# Struct pointer declarations
PPROCESSENTRY32 = LPPROCESSENTRY32 = POINTER(PROCESSENTRY32)
PTHREADENTRY32 = LPTHREADENTRY32 = POINTER(THREADENTRY32)
LPPROCESS_INFORMATION = POINTER(PROCESS_INFORMATION)
LPSECURITY_ATTRIBUTES = POINTER(SECURITY_ATTRIBUTES)
LPMODULEINFO = POINTER(MODULEINFO)

#######################
# Function Prototypes #
#######################


LoadLibraryA = kernel32.LoadLibraryA
LoadLibraryW = kernel32.LoadLibraryW
LoadLibraryExA = kernel32.LoadLibraryExA
LoadLibraryExW = kernel32.LoadLibraryExW

LoadLibraryExW.restype = LoadLibraryExA.restype = LoadLibraryW.restype = LoadLibraryA.restype = HMODULE

exArgs = lambda b: b.argtypes + [ HANDLE, DWORD ]
LoadLibraryA.argtypes = [ LPCSTR ]
LoadLibraryW.argtypes = [ LPCWSTR ]
LoadLibraryExA.argtypes = exArgs(LoadLibraryA)
LoadLibraryExW.argtypes = exArgs(LoadLibraryW)
del exArgs

LoadLibraryA.__doc__ = \
LoadLibraryW.__doc__ = \
LoadLibraryExA.__doc__ = \
LoadLibraryExW.__doc__ = \
""" Loads the specified module into the address space of the calling process. The specified module may cause other
modules to be loaded. """

PLoadLibraryA = cast(LoadLibraryA, LPTHREAD_START_ROUTINE)
PLoadLibraryW = cast(LoadLibraryW, LPTHREAD_START_ROUTINE)

FreeLibrary = kernel32.FreeLibrary
FreeLibrary.restype = BOOL
FreeLibrary.argtypes = [ HMODULE ]
FreeLibrary.__doc__ = """ Frees the loaded dynamic-link library (DLL) module and, if necessary, decrements its
reference count. When the reference count reaches zero, the module is unloaded from the address space of the
calling process and the handle is no longer valid. """

PFreeLibrary = cast(FreeLibrary, LPTHREAD_START_ROUTINE)

FreeLibraryAndExitThread = kernel32.FreeLibraryAndExitThread
FreeLibraryAndExitThread.restype = None
FreeLibraryAndExitThread.argtypes = [ HMODULE, DWORD ]
FreeLibraryAndExitThread.__doc__ = """ Decrements the reference count of a loaded dynamic-link library (DLL) by
one, then calls ExitThread to terminate the calling thread. The function does not return."""

GetModuleHandleA = kernel32.GetModuleHandleA
GetModuleHandleW = kernel32.GetModuleHandleW

GetModuleHandleW.restype = GetModuleHandleA.restype = HMODULE
GetModuleHandleA.argtypes = [ LPCSTR ]
GetModuleHandleW.argtypes = [ LPCWSTR ]

GetModuleHandleA.__doc__ = \
GetModuleHandleW.__doc__ = \
""" Retrieves a module handle for the specified module. The module must have been loaded by the calling process. """

GetModuleHandleExA = kernel32.GetModuleHandleExA
GetModuleHandleExW = kernel32.GetModuleHandleExW

GetModuleHandleExW.restype = GetModuleHandleExA = BOOL
GetModuleHandleExA.argtypes = [ DWORD, LPCSTR, POINTER(HMODULE) ]
GetModuleHandleExW.argtypes = [ DWORD, LPCWSTR, POINTER(HMODULE) ]

GetModuleHandleExA.__doc__ = \
GetModuleHandleExW.__doc__ = \
""" Retrieves a module handle for the specified module and increments the module's reference count unless
GET_MODULE_HANDLE_EX_FLAG_UNCHANGED_REFCOUNT is specified. The module must have been loaded by the calling process. """

GetProcAddress = kernel32.GetProcAddress
GetProcAddress.restype = FARPROC
GetProcAddress.argtypes = [ HMODULE, LPCSTR ]
GetProcAddress.__doc__ = \
""" Retrieves the address of an exported function or variable from the specified dynamic-link library (DLL). """

CreateToolhelp32Snapshot = kernel32.CreateToolhelp32Snapshot
CreateToolhelp32Snapshot.restype = HANDLE
CreateToolhelp32Snapshot.argtypes = [DWORD, DWORD]
CreateToolhelp32Snapshot.__doc__ = \
""" Takes a snapshot of the specified processes, as well as the heaps, modules, and threads used by these processes. """

# TODO: Might want to reimplment the toolhelp snapshot functions as their unicode counterparts
Process32First = kernel32.Process32First
Process32First.restype = BOOL
Process32First.argtypes = [HANDLE, LPPROCESSENTRY32]
Process32First.__doc__ = \
"""BOOL Process32First(HANDLE hSnapshot, LPPROCESSENTRY32 lppe)
ppython.h:91"""

Process32Next = kernel32.Process32Next
Process32Next.restype = BOOL
Process32Next.argtypes = [HANDLE, LPPROCESSENTRY32]
Process32Next.__doc__ = \
"""BOOL Process32Next(HANDLE hSnapshot, LPPROCESSENTRY32 lppe)
ppython.h:91"""

Thread32First = kernel32.Thread32First
Thread32First.restype = BOOL
Thread32First.argtypes = [HANDLE, LPTHREADENTRY32]
Thread32First.__doc__ = \
"""BOOL Thread32First(HANDLE hSnapshot, LPTHREADENTRY32 lpte)
ppython.h:93"""

Thread32Next = kernel32.Thread32Next
Thread32Next.restype = BOOL
Thread32Next.argtypes = [HANDLE, LPTHREADENTRY32]
Thread32Next.__doc__ = \
"""BOOL Thread32Next(HANDLE hSnapshot, LPTHREADENTRY32 lpte)
ppython.h:93"""

GetCurrentProcessId = kernel32.GetCurrentProcessId
GetCurrentProcessId.restype = DWORD
GetCurrentProcessId.argtypes = []
GetCurrentProcessId.__doc__ = \
"""DWORD GetCurrentProcessId()
ppython.h:94"""

OpenProcess = kernel32.OpenProcess
OpenProcess.restype = HANDLE
OpenProcess.argtypes = [DWORD, BOOL, DWORD]
OpenProcess.__doc__ = \
"""HANDLE OpenProcess(DWORD dwDesiredAccess, BOOL bInheritHandle, DWORD dwProcessId)
ppython.h:96"""

WriteProcessMemory = kernel32.WriteProcessMemory
WriteProcessMemory.restype = BOOL
WriteProcessMemory.argtypes = [HANDLE, LPVOID, LPCVOID, SIZE_T, POINTER(SIZE_T)]
WriteProcessMemory.__doc__ = \
"""BOOL WriteProcessMemory(HANDLE hProcess, LPVOID lpBaseAddress, LPCVOID lpBuffer, SIZE_T nSize, SIZE_T * lpNumberOfBytesWritten)
ppython.h:86"""

VirtualAllocEx = kernel32.VirtualAllocEx
VirtualAllocEx.restype = LPVOID
VirtualAllocEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD, DWORD]
VirtualAllocEx.__doc__ = \
"""LPVOID VirtualAllocEx(HANDLE hProcess, LPVOID lpAddress, SIZE_T dwSize, DWORD flAllocationType, DWORD flProtect)
ppython.h:87"""

VirtualFreeEx = kernel32.VirtualFreeEx
VirtualFreeEx.restype = BOOL
VirtualFreeEx.argtypes = [HANDLE, LPVOID, SIZE_T, DWORD]
VirtualFreeEx.__doc__ = \
"""BOOL VirtualFreeEx(HANDLE hProcess, LPVOID lpAddress, SIZE_T dwSize, DWORD dwFreeType)
ppython.h:88"""

CreateRemoteThread = kernel32.CreateRemoteThread
CreateRemoteThread.restype = HANDLE
CreateRemoteThread.argtypes = [HANDLE, LPSECURITY_ATTRIBUTES, SIZE_T, LPTHREAD_START_ROUTINE, LPVOID, DWORD, LPDWORD]
CreateRemoteThread.__doc__ = \
"""HANDLE CreateRemoteThread(HANDLE hProcess, LPSECURITY_ATTRIBUTES lpThreadAttributes, SIZE_T dwStackSize, LPTHREAD_START_ROUTINE lpStartAddress, LPVOID lpParameter, DWORD dwCreationFlags, LPDWORD lpThreadId)
ppython.h:97"""

GetExitCodeThread = kernel32.GetExitCodeThread
GetExitCodeThread.restype = BOOL
GetExitCodeThread.argtypes = [HANDLE, LPDWORD]

WaitForSingleObject = kernel32.WaitForSingleObject
WaitForSingleObject.restype = DWORD
WaitForSingleObject.argtypes = [HANDLE, DWORD]
WaitForSingleObject.__doc__ = \
"""DWORD WaitForSingleObject(HANDLE hHandle, DWORD dwMilliseconds)
ppython.h:98"""

CloseHandle = kernel32.CloseHandle
CloseHandle.restype = BOOL
CloseHandle.argtypes = [HANDLE]
CloseHandle.__doc__ = \
"""BOOL CloseHandle(HANDLE hObject)
ppython.h:100"""


# These two functions are setup below.
GetModuleFileNameA = kernel32.GetModuleFileNameA
GetModuleFileNameW = kernel32.GetModuleFileNameW

# On Windows 7 and Windows Server 2008 R2, the functions below are exported from kernel32.dll. On
# Windows Server 2008, Windows Vista, Windows Server 2003, and Windows XP, though, they're exported
# from psapi.dll.
_exdll = kernel32
def _psapifunc(fname):
	global _exdll
	try: return getattr(_exdll, fname)
	except:
		try: return getattr('K32' + _exdll, fname)
		except:
			if 'psapi' in _exdll._name: raise
			_exdll = WinDLL('psapi.dll')
			return _psapifunc(fname)

GetModuleFileNameExA = _psapifunc('GetModuleFileNameExA')
GetModuleFileNameExW = _psapifunc('GetModuleFileNameExW')

GetModuleFileNameExW.restype = GetModuleFileNameExA.restype = GetModuleFileNameW.restype = GetModuleFileNameA.restype = DWORD

GetModuleFileNameA.argtypes = [ HMODULE, LPSTR, DWORD ]
GetModuleFileNameW.argtypes = [ HMODULE, LPWSTR, DWORD]
GetModuleFileNameExA.argtypes = [ HANDLE ] + GetModuleFileNameA.argtypes
GetModuleFileNameExW.argtypes = [ HANDLE ] + GetModuleFileNameW.argtypes

GetModuleFileNameA.__doc__ = \
GetModuleFileNameW.__doc__ = \
GetModuleFileNameExA.__doc__ = \
GetModuleFileNameExW.__doc__ = \
""" Retrieves the fully qualified path for the file containing the specified module. """

def GetModuleFileName(handle):
	""" Wrapper around GetModuleFileNameW to handle allocating our buffer. """
	buf = create_unicode_buffer(MAX_PATH + 1)
	if GetModuleFileNameW(handle, buf, MAX_PATH) == 0:
		del buf
		return None
	return buf.value

GetModuleInformation = _psapifunc('GetModuleInformation')
GetModuleInformation.restype = BOOL
GetModuleInformation.argtypes = [ HANDLE, HMODULE, LPMODULEINFO, DWORD ]
GetModuleInformation.__doc__ = """ Retrieves information about the specified module in the MODULEINFO structure. """

GetProcessImageFileNameA = _psapifunc('GetProcessImageFileNameA')
GetProcessImageFileNameW = _psapifunc('GetProcessImageFileNameW')

GetProcessImageFileNameW.restype = GetProcessImageFileNameA.restype = DWORD
GetProcessImageFileNameA.argtypes = [ HANDLE, LPSTR, DWORD ]
GetProcessImageFileNameW.argtypes = [ HANDLE, LPWSTR, DWORD ]
GetProcessImageFileNameA.__doc__ = \
GetProcessImageFileNameW.__doc__ = """ Retrieves the name of the executable file for the specified process. """

EnumProcesses = _psapifunc('EnumProcesses')
EnumProcesses.restype = BOOL
EnumProcesses.argtypes = [ LPDWORD, DWORD, LPDWORD ]
EnumProcesses.__doc__ = """ Retrieves the process identifier for each process object in the system. """

EnumProcessModules = _psapifunc('EnumProcessModules')
EnumProcessModulesEx = _psapifunc('EnumProcessModulesEx')

EnumProcessModulesEx.restype = EnumProcessModules.restype = BOOL
EnumProcessModules.argtypes = [ HANDLE, HMODULE, DWORD, LPDWORD ]
EnumProcessModulesEx.argtypes = EnumProcessModules.argtypes + [ DWORD ]

EnumProcessModules.__doc__ = """ Retrieves a handle for each module in the specified process. """
EnumProcessModulesEx.__doc__ = """ Retrieves a handle for each module in the specified process that meets the specified filter criteria. """

_GetCurrentProcess = kernel32.GetCurrentProcess
_GetCurrentProcess.restype = HANDLE
_GetCurrentProcess.argtypes = [ ]

_ReadProcessMemory = kernel32.ReadProcessMemory
_ReadProcessMemory.restype = BOOL
_ReadProcessMemory.argtypes = [ HANDLE, LPCVOID, LPVOID, SIZE_T, POINTER(SIZE_T) ]

_currproc = _GetCurrentProcess()
def GetCurrentProcess():
	""" Retrieves a pseudo handle for the current process. """
	global _currproc
	return _currproc

_procbase = GetModuleHandleA(cast(NULL, c_char_p))
def GetModuleHandle():
	global _procbase
	return _procbase

def ReadProcessMemory(size, base = None, handle = None):
	if handle is None:
		handle = GetCurrentProcess()
	if base is None:
		base = GetModuleHandle()
	elif type(base) != c_void_p:
		base = cast(base, c_void_p)
	buff = (c_ubyte * size)()
	sz = SIZE_T(size)
	if not bool(_ReadProcessMemory(handle, base, cast(buff, LPVOID), sz, byref(sz) )):
		del buff
		return None
	try:
		resize(buff, sz.value)
	except:
		pass
	result = string_at(buff, sz.value)
	del buff, sz
	return result

ReadProcessMemory.__doc__ = """ Reads data from an area of memory in a specified process. The entire area to be read must be accessible or the operation fails. """

# Helper declarations
NULL_SECURITY_ATTRIBUTES = cast(NULL, LPSECURITY_ATTRIBUTES)
SZPROCESSENTRY = sizeof(PROCESSENTRY32)
SZTHREADENTRY = sizeof(THREADENTRY32)

# Size stuff
def limits(typ):
	umin = 0
	umax = (256 ** sizeof(typ))
	max = (umax / 2) - 1
	min = (max * -1)
	umax -= 1
	return min, max, umin, umax

c_short_min, c_short_max, c_ushort_min, c_ushort_max = limits(c_short)
c_int_min, c_int_max, c_uint_min, c_uint_max = limits(c_int)
c_long_min, c_long_max, c_ulong_min, c_ulong_max = limits(c_long)
