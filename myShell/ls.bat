@echo off
set location=%0
set action=%1
python "%location%\ls.py %action%"
exit