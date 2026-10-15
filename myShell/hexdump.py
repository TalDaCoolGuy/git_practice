import os
import sys

if len(sys.argv) > 1 and sys.argv[1].strip():
    path = str(sys.argv[1]).strip()
else:
    path = False

data = "not allowed input idk"
if path:
    if not os.path.exists(path):
        if os.path.exists(f"{os.getcwd()}\\path"):
            path = f"{os.getcwd()}\\path"
        else:
            path = False

if path:
    with open(path, "rb") as f:
        data = f.read().hex()

with open(f"output.txt","wt") as f:
    f.write(data)