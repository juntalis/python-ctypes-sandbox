@echo off
if not "%PROCESSOR_ARCHITECTURE%"=="x86" (
rem Changed to /K to allow seeing how changes affected the command prompt post-run
"%WinDir%\SysWOW64\cmd.exe" /K "%~dpnx0"
if errorlevel 1 exit /B %ERRORLEVEL%
exit /B 0
)

setlocal
goto Main

:FindCmd
set ENVSETUP=%~$PATH:1
goto :EOF

:Main
call :FindCmd x86env.bat
if "%ENVSETUP%x"=="x" call :FindCmd x86env.cmd
if not "%ENVSETUP%x"=="x" call "%ENVSETUP%"
python.exe -B -u "%~dp0rpython.py"
if errorlevel 1 (
	pause
	exit /B %ERRORLEVEL%
)
endlocal