@echo off
color A


echo Checking unlocked desktop ...
:bureau
tasklist | find /i "explorer.exe" > nul && goto :bureau_fin
timeout /t 1 /nobreak > nul
goto :bureau
:bureau_fin
echo Desktop unlocked
echo.

echo Checking Internet connection ...
:internet
ping -n 1 8.8.8.8 > nul
if errorlevel 1 (
	echo No Internet connection
	timeout /t 1 /nobreak > nul
	goto internet
)
echo Established Internet connection
echo.


echo Check if curl is installed ...
curl --version >nul 2>&1
if %errorlevel% == 1 (
	echo No Internet connection
	pause
	exit
)
echo.

echo Sending start message ...
set "BOT_API_KEY=5889004504:AAF-mKs2KENoSgEyYR0TV89sQbsxjLdKVPE"
set "CHAT_ID=-1001514266177"
set "MESSAGE=D\u00E9but du scraping"
curl -k -X POST "https://api.telegram.org/bot%BOT_API_KEY%/sendMessage" -H "Content-Type: application/json" -d "{\"chat_id\":%CHAT_ID%,\"text\":\"%MESSAGE%\"}"
echo Start message sent
echo.

echo Checking installation of Python ...
setlocal enableextensions
set PYTHON_EXE=python.exe
for %%i in (%PYTHON_EXE%) do (
    set PYTHON_PATH=%%~$PATH:i
)
if "%PYTHON_PATH%"=="" (
    echo Please install the latest version of Python on this computer or, if it doesn't work, install Python 3.11.2
    endlocal
    pause
    exit
) else (
    echo Python is installed
)
endlocal
echo.

echo Checking required packages ...
pip show selenium > nul 2>&1 || (
	echo Installing selenium ...
	pip install selenium
	echo selenium installed
)

pip show requests > nul 2>&1 || (
	echo Installing requests ...
	pip install requests
	echo requests installed
)

@REM pip show install python-telegram-bot > nul 2>&1 || (
@REM 	echo Installing python-telegram-bot ...
@REM 	pip install python-telegram-bot
@REM 	echo python-telegram-bot installed
@REM )
echo Required packages installed
echo.

tasklist | find /i "geckodriver.exe" && (
	echo geckodriver is already running
) || (
	echo Launching geckodriver ...
	start /min "" "C:\Users\Leboncoin\Desktop\Winamax\geckodriver.exe"
	echo geckodriver launched
)
echo.

echo Launching main code ...
"C:\Python\python.exe" "C:\Users\Leboncoin\Desktop\Winamax\main.py"
echo Main code ended
echo.

echo Sending end message ...
set "MESSAGE=Fin du scraping"
curl -k -X POST "https://api.telegram.org/bot%BOT_API_KEY%/sendMessage" -H "Content-Type: application/json" -d "{\"chat_id\":%CHAT_ID%,\"text\":\"%MESSAGE%\"}"
echo End message sent
echo.

echo End of setup code
pause
exit
