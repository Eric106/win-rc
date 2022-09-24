rm dist/win-rc/ -rf 
pyinstaller win-rc.py -y
robocopy keys\ dist\win-rc\keys\ /e
robocopy bin\ dist\win-rc\bin\ /e
robocopy downloads\ dist\win-rc\downloads\ /e
copy bin\run_tunn.bat dist\win-rc\
copy bin\setup.bat dist\win-rc\
