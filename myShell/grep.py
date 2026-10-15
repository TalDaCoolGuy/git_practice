import os
import sys

if len(sys.argv) > 2 and sys.argv[1].strip() and sys.argv[2].strip():
    data = str(sys.argv[1])
    path = str(sys.argv[2])
else:
    data = False
    path = False# i dont really need to put it but if i dont, i will get a warning


output = "not allowed input idk"
ispath = True
if path:
    if not os.path.exists(path):
        if os.path.exists(f"{os.getcwd()}\\{path}"):
            path = f"{os.getcwd()}\\{path}"
        else:
            ispath = False
else:
    ispath = False

if ispath:
    with open(path, "rt") as f:
        path = f.read()
if ispath:
    output = ""
    path = path.split("\n")
    i = 0
    for line in path:
        if data in line:
            output += f"line{i}: {line}\n"
        i+=1
    output = output.rstrip("\n")  # remove the last \n because for some reson i cant do -= :(

with open(f"output.txt","wt") as f:
    f.write(output)