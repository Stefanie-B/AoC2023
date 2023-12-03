fname = "input"

maxvals = {"red": 12, "green": 13, "blue": 14}

f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()
total = 0
for i, line in enumerate(lines):
    possible = True
    game, blocks = line.strip("\n").split(":")
    grabs = blocks.split(";")
    for grab in grabs:
        for colorgrab in grab.split(", "):
            number, color = colorgrab.lstrip(" ").rstrip(" ").split(" ")
            if int(number) > maxvals[color]:
                possible = False
    if possible:
        total += i + 1
print(total)
