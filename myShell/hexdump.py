import os
import sys

if len(sys.argv) > 1 and sys.argv[1].strip():
    path = str(sys.argv[1].strip())
else:
    path = False
if path:
    if not os.path.exists(path):
        if os.path.exists(f"{os.getcwd()}\\path"):
            path = f"{os.getcwd()}\\path"
        else:
            path = False
    if path:
        if os.path.isdir(path):
            data = os.listdir(path)
        else:
            data = False
    else:
        data = False
else:
    data = os.listdir(os.getcwd())

output = ""
if data:
    for i in data:
        output += f"{i}\n"
else:
    output = "not allowed input idk"
output = output.rstrip("\n")#remove the last \n because for some reson i cant do -= :(
with open(f"output.txt","wt") as f:
    f.write(output)