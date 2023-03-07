@echo off
color A


@REM Obtenir les droits administrateur
set "params=%*"
cd /d "%~dp0" && ( if exist "%temp%\getadmin.vbs" del "%temp%\getadmin.vbs" ) && fsutil dirty query %systemdrive% 1>nul 2>nul || ( echo Set UAC = CreateObject^("Shell.Application"^) : UAC.ShellExecute "cmd.exe", "/k cd ""%~sdp0"" && %~s0 %params%", "", "runas", 1 >> "%temp%\getadmin.vbs" && "%temp%\getadmin.vbs" && exit /B )

set "source=C:\Users\Leboncoin\Desktop\Winamax\setup.bat"
set "destination=C:\ProgramData\Microsoft\Windows\Start Menu\Programs\Startup\Winamax.lnk"

@REM Création du raccourci
echo Cration du raccourci ...
set "script="%temp%\shortcut.vbs""
echo Set oWS = WScript.CreateObject("WScript.Shell") > %script%
echo sLinkFile = "%destination%" >> %script%
echo Set oLink = oWS.CreateShortcut(sLinkFile) >> %script%
echo oLink.TargetPath = "%source%" >> %script%
echo oLink.Save >> %script%
cscript /nologo %script%
del %script%
echo Raccourci créé