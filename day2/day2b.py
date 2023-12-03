import numpy as np

fname = "input"


f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()
total = 0
for i, line in enumerate(lines):
    maxvals = {"red": 0, "green": 0, "blue": 0}
    game, blocks = line.strip("\n").split(":")
    grabs = blocks.split(";")
    for grab in grabs:
        for colorgrab in grab.split(", "):
            number, color = colorgrab.lstrip(" ").rstrip(" ").split(" ")
            if int(number) > maxvals[color]:
                maxvals[color] = int(number)

    power = np.prod(list(maxvals.values()))
    total += power

print(total)
