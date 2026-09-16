@echo off
cd /d "%~dp0"
python -m PyInstaller --onefile --windowed --name "EME-LogicAlgo" --icon "resources\favicon.ico" --add-data "resources\LogoEME.png:." --add-data "resources\favicon.ico:." logicalgo_eme.py
pause
