from subprocess import run
from os import makedirs
from os import path
makedirs("rules", exist_ok=True)
with open("rules.txt", "r") as file:
    for line in file.readlines():
        url, name = line.strip().split()
        run(["wget", "-O", path.join("rules", name), url])