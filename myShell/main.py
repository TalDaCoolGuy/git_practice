import os
import subprocess

current_dir = os.path.dirname(__file__)
#"hello","ls","hexdump","grep","cd"]

while True:
    cmd = input(f"{os.getcwd()}>>>")

    if cmd == "exit":
        exit("bye")
    cmds = cmd.split("|")

    for cmd in cmds:
        cmd = cmd.split()
        data = b""
        with open("output.txt","rb") as f:
            data = f.read()
        if cmd[0] == "hello":
            subprocess.call(f"{current_dir}\\hello.bat {current_dir}", shell=True,)
        elif cmd[0] == "ls":
            if len(cmd) == 1:
                if len(data) > 0:
                    subprocess.call(f"{current_dir}\\ls.bat {data}", shell=True,)
                else:
                    subprocess.call(f"{current_dir}\\ls.bat {current_dir}", shell=True,)

            elif len(cmd) == 2:
                subprocess.call(f"{current_dir}\\ls.bat {current_dir}", shell=True,)
            else:
                print("not allowed input idk")
                break

        else:
            print("not allowed input idk")
            break
