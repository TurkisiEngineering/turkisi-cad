@echo off
rem Kontrol paneli: sunucuyu ayri bir pencerede acar, sonra tarayiciyi acar.
rem Demo (kuru) mod:  PANEL.bat --kuru      Baska port:  PANEL.bat --kuru --port 8799
cd /d "%~dp0"
set PORT=8765
:ara
if "%~1"=="" goto bitti
if "%~1"=="--port" set PORT=%~2
shift
goto ara
:bitti
start "" /min cmd /c "python -X utf8 panel_sunucu.py %* & pause"
timeout /t 2 /nobreak >nul
start "" http://127.0.0.1:%PORT%/
