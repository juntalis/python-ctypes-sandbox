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

static HANDLE hConsole = NULL;
static LPCSTR msgParent = "\nSOURCE: ";
static LPCSTR msgText = "\nMSGTXT: ";

static void writeMessage(LPCSTR prefix, LPCSTR message)
{
	SIZE_T buffLen;
	
	// Verify hConsole
	if(hConsole == NULL) {
		if((hConsole = CreateFile("CONOUT$", GENERIC_WRITE | GENERIC_READ, FILE_SHARE_READ | FILE_SHARE_WRITE, 0L, OPEN_EXISTING, FILE_ATTRIBUTE_NORMAL, 0L)
		) == INVALID_HANDLE_VALUE) {
			MessageBoxA(NULL, "Failed to get STDOUT!", "Error", MB_OK|MB_ICONERROR);
		}
	}
	
	// Write the first part of the line.
	SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 15));
	buffLen = 9 * sizeof(const char);
	WriteFile(hConsole, (LPCVOID)prefix, (DWORD)buffLen, NULL, NULL);
	
	// Write our message
	SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 10));
	buffLen = (lstrlenA(message)) * sizeof(const char);
	WriteFile(hConsole, (LPCVOID)message, (DWORD)buffLen, NULL, NULL);
	
	// Reset to default.
	SetConsoleTextAttribute( hConsole, (WORD)((0 << 4) | 7));
}

void __declspec(dllexport) Finalize()
{
	char sModulePath[MAX_PATH + 1] = "";
	GetModuleFileNameA(NULL, sModulePath, MAX_PATH);
	writeMessage(msgParent, sModulePath);
	writeMessage(msgText, "Goodbye World\n");
}

void __declspec(dllexport) Initialize()
{
	char sModulePath[MAX_PATH + 1] = "";
	GetModuleFileNameA(NULL, sModulePath, MAX_PATH);
	writeMessage(msgParent, sModulePath);
	writeMessage(msgText, "Hello World\n");
}

BOOL WINAPI DllMain( HINSTANCE hInstance, DWORD dwReason, LPVOID lpReserved )
{
	return TRUE;
}