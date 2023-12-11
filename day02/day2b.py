import numpy as np

# Read-in input
fname = "day02/input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

# assume the game is possible for all games, only change this if you find too many cubes
total = 0
for i, line in enumerate(lines):
    # We initialize an empty set
    maxvals = {"red": 0, "green": 0, "blue": 0}

    # Separate the game number and the numbers of cubes in all grabs (a block)
    game, blocks = line.strip("\n").split(":")

    # Separate the block of cube numbers into different sets of grabs from the bag
    grabs = blocks.split(";")
    for grab in grabs:
        # For each grab from the bag, update the maximum of a color if it has been exceeded
        for colorgrab in grab.split(", "):
            number, color = colorgrab.lstrip(" ").rstrip(" ").split(" ")
            if int(number) > maxvals[color]:
                maxvals[color] = int(number)
    # The power is the product of the minimum needed number of cubes per color, we sum the power
    # each set
    power = np.prod(list(maxvals.values()))
    total += power
print(total)
