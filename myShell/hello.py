import os
current_dir = os.path.dirname(__file__)

username = os.getlogin()

with open(f"{current_dir}\\output.txt","wt") as f:
    f.write(f"hello {username}")