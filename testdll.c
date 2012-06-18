#pragma comment(lib,"user32.lib")
#pragma comment(lib,"Advapi32.lib")

// Speed up build process with minimal headers.
#define WIN32_LEAN_AND_MEAN
#define VC_EXTRALEAN
#include <SDKDDKVer.h>
#include <windows.h>
#include <stdlib.h>
#include <stdio.h>
#include <malloc.h>

HMODULE GetCurrentModule()
{ // NB: XP+ solution!
	HMODULE hModule = NULL;
	GetModuleHandleEx(
		GET_MODULE_HANDLE_EX_FLAG_FROM_ADDRESS,
		(LPCTSTR)GetCurrentModule,
		&hModule);

	return hModule;
}

BOOL WINAPI DllMain( HINSTANCE hInstance, DWORD dwReason, LPVOID lpReserved )
{
	BOOL bResult = FALSE;
	HANDLE hConsole;
	LPCSTR msgCommon = "PARENT: ",
	msgAttach = "Hello World\n",
	msgDetach = "Goodbye World\n";

	SIZE_T buffLen;
	AttachConsole((DWORD)-1);
	if((hConsole = CreateFile("CONOUT$", GENERIC_WRITE | GENERIC_READ,
		FILE_SHARE_READ | FILE_SHARE_WRITE,
		0L, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0L)
	) == INVALID_HANDLE_VALUE) {
		MessageBoxA(NULL, "Failed to get STDOUT!", "Error", MB_OK|MB_ICONERROR);
	}
	
	SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 15));
	buffLen = (lstrlenA(msgCommon)) * sizeof(const char);
	WriteFile(hConsole, (LPCVOID)msgCommon, (DWORD)buffLen, NULL, NULL);
	
	SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 10));
	if (dwReason == DLL_PROCESS_ATTACH)
	{
		buffLen = (lstrlenA(msgAttach)) * sizeof(const char);
		WriteFile(hConsole, (LPCVOID)msgAttach, (DWORD)buffLen, NULL, NULL);
		SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 7));
	} else if (dwReason == DLL_PROCESS_DETACH) {
		buffLen = (lstrlenA(msgDetach)) * sizeof(const char);
		WriteFile(hConsole, (LPCVOID)msgDetach, (DWORD)buffLen, NULL, NULL);
		SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 7));
	}
	return bResult;
}