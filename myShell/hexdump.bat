@echo off
set location=%1
set action=%2
python "%location%\hexdump.py" %action%
exit