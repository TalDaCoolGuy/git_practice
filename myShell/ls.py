import os

data = os.listdir(os.getcwd())#getcwd() is where i started the main.py, its not where is the ls file located but where i started it in the cmd

with open(f"output.txt","wt") as f:
    f.write(str(data))
for i in data:
    print(i)