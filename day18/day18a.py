import numpy as np
from matplotlib import pyplot as plt

pointing = {"R": [0, 1], "L": [0, -1], "U": [-1, 0], "D": [1, 0]}

# Load in the text, discard endlines
fname = "input"
f = open(f"day18/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

field = np.array([[True]])
headcoord = np.array([0, 0])
for line in lines:
    direction, distance, color = line.split(" ")
    for step in range(int(distance)):
        headcoord += pointing[direction]
        sizey, sizex = field.shape
        if (not 0 <= headcoord[0] < sizey) and direction == "D":
            field = np.append(field, np.tile([False], (1, sizex)), axis=0)
        elif (not 0 <= headcoord[0] < sizey) and direction == "U":
            field = np.insert(field, [0], np.tile([False], (1, sizex)), axis=0)
            headcoord[0] = 0
        elif (not 0 <= headcoord[1] < sizex) and direction == "R":
            field = np.append(field, np.tile([False], (sizey, 1)), axis=1)
        elif (not 0 <= headcoord[1] < sizex) and direction == "L":
            field = np.insert(field, [0], np.tile([False], (sizey, 1)), axis=1)
            headcoord[1] = 0
        field[headcoord[0], headcoord[1]] = True

plt.close()
plt.figure()
plt.title(line)
plt.imshow(field)
plt.show()


def check_pixel(field, pit, y, x):
    y %= field.shape[0]
    x %= field.shape[1]
    pitpix = pit[y, x]
    fieldpix = field[y, x]
    if not np.isnan(pitpix) and not fieldpix:
        pit[y, x] = np.nan
    return pit


pit = np.ones_like(field) * np.nan
pit[1:-1, 1:-1] = 1
pit[np.where(field)] = 1
sizey, sizex = field.shape
visited = []

oldpit = np.zeros_like(pit)
while not np.all(np.isnan(pit) == np.isnan(oldpit)):
    mask = (np.isnan(pit)) * (~np.isnan(oldpit))
    oldpit = pit.copy()
    ycoord, xcoord = np.where(mask)
    for y, x in zip(ycoord, xcoord):
        pit = check_pixel(field, pit, y + 1, x)
        pit = check_pixel(field, pit, y - 1, x)
        pit = check_pixel(field, pit, y, x - 1)
        pit = check_pixel(field, pit, y, x + 1)

plt.close()
plt.figure()
plt.title(f"checking {len(ycoord)}")
plt.imshow(pit)
plt.show()


print(np.sum(~np.isnan(pit)))
