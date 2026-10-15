import os

username = os.getlogin()

with open("output.txt","wt") as f:
    f.write(f"hello {username}")