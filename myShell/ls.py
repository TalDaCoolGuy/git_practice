import os
import sys

path = str(sys.argv[1])
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

with open(f"output.txt","wt") as f:
    f.write(output)