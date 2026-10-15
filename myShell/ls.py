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
        data = os.listdir(path)
    else:
        data = "cant open that"
else:
    data = os.listdir(os.getcwd())

output = ""

for i in data:
    output += f"{i}\n"
output = output.rstrip("\n")#remove the last \n because for some reson i cant do -= :(
with open(f"output.txt","wt") as f:
    f.write(output)