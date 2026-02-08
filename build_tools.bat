@echo off
echo ================================
echo Building OSINT Tools EXE
echo ================================

pyinstaller ^
 --onefile ^
 --windowed ^
 --name OSINT_Tools ^
 --add-data "blackbird;blackbird" ^
 --add-data "sherlock;sherlock" ^
 --add-data "maigret;maigret" ^
 osint_launcher.py

echo.
echo Build finished.
echo File is in /dist folder
pause
