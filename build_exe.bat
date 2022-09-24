rm dist/win-rc/ -rf 
pyinstaller win-rc.py -y
robocopy keys\ dist\win-rc\keys\ /e
robocopy ssh\ dist\win-rc\ssh\ /e
