@echo off
echo You only need to run this file once
echo installing packages
pip install pillow
pip install pywin32
pip install keyboard
pip install pyautogui
pip install opencv-python

echo Installed Packages

echo running Bot
python main.py

pause