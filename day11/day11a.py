# We use numpy to be able to use array indexing
import numpy as np


def expand_coords(coords):
    """
    Calculates the galaxy coordinates along 1 axis after expansion. This is done by finding positions
    along the axis devoid of galaxies and doubling this empty space

    Parameters
    ----------
    coords : list of ints
        coordinates of galaxies along x or y axis

    Returns
    -------
    list of ints
        coordinates of galaxies along the same axis, after expansion
    """
    # create a list of empty spaces along this axis
    empty_list = [i for i in range(max(coords) + 1) if i not in coords]

    # we convert to numpy arrays in order to use masking
    coords = np.array(coords)

    # move through the empty spaces big to small, so we do not accidentally move galasxies more tha
    # once if they pass a previously empty line during expansion
    for empty_space in empty_list[::-1]:
        coords[coords > empty_space] += 1
    return list(coords)


# Load in the text, discard endlines
fname = "day11/input"
f = open(f"{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

# We collect the coordinates of all galaxies, separated in x and y
xcoords = []
ycoords = []
for row, line in enumerate(lines):
    for column, char in enumerate(line):
        if char == "#":
            xcoords.append(column)
            ycoords.append(row)

# we move the galaxies according to the expansion of the Universe
ycoords = expand_coords(ycoords)
xcoords = expand_coords(xcoords)

# go through all pairs and add the distance, which is just the absolute difference between the
# coordinates in this Manhatten metric
total = 0
for i in range(len(xcoords)):
    for j in range(i + 1, len(xcoords)):
        total += abs(xcoords[i] - xcoords[j]) + abs(ycoords[i] - ycoords[j])

print(total)
