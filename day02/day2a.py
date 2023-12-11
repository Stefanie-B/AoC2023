# Read-in input
fname = "day02/input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

# Maximum number of cubes per color for a game to be possible
maxvals = {"red": 12, "green": 13, "blue": 14}

# assume the game is possible for all games, only change this if you find too many cubes
total = 0
for i, line in enumerate(lines):
    possible = True

    # Separate the game number and the numbers of cubes in all grabs (a block)
    game, blocks = line.strip("\n").split(":")

    # Separate the block of cube numbers into different sets of grabs from the bag
    grabs = blocks.split(";")
    for grab in grabs:
        # For each grab from the bag, check if the maximum for the color hasn't been exceeded
        for colorgrab in grab.split(", "):
            number, color = colorgrab.lstrip(" ").rstrip(" ").split(" ")
            if int(number) > maxvals[color]:
                possible = False
                break
    # If we've never exceeded the max number, we can add the game number, which is one higher than
    # the line number
    if possible:
        total += i + 1
print(total)
