import os
import subprocess

current_dir = os.path.dirname(__file__)
cmds = ["uwu","ls"]#,"hello","hexdump","grep","cd"

while True:
    cmd = input(">>>")
    if cmd == "exit":
        exit("bye")
    elif cmd in cmds:
        subprocess.call(f"{current_dir}\\{cmd}.bat {current_dir}", shell=True,)
    else:
        print("not allowed input idk")
