@ECHO OFF
setlocal
set VARS_SET=0
if not "%VS100COMNTOOLS%x"=="x" ((call "%VS100COMNTOOLS%\..\..\VC\vcvarsall.bat" x86) && (set VARS_SET=1))
if "%VARS_SET%"=="0" (
	if not "%VS90COMNTOOLS%x"=="x" ((call "%VS90COMNTOOLS%\..\..\VC\vcvarsall.bat" x86) && (set VARS_SET=1))
)
if "%VARS_SET%"=="0" (
	if not "%VS80COMNTOOLS%x"=="x" ((call "%VS80COMNTOOLS%\..\..\VC\vcvarsall.bat" x86) && (set VARS_SET=1))
)
if not exist "%~dp0obj" mkdir "%~dp0obj"
cl -O2 "-Fo%~dp0obj\testdll.obj" "testdll.c" -link -DLL -OPT:REF -OPT:ICF "-OUT:testdll.dll" "-IMPLIB:%~dp0obj\testdll.lib"
endlocal