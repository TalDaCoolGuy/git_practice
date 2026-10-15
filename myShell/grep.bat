@echo off
set location=%1
set data=%2
set pathh=%3
python "%location%\grep.py" %data% %pathh%
exit