# We use numpy to be able to use array indexing
import numpy as np
from matplotlib import pyplot as plt

# Load in the text, discard endlines
fname = "input"
f = open(f"day10/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

start_y = np.squeeze([i for i, line in enumerate(lines) if "S" in line])
start_x = np.squeeze([i for i, char in enumerate(lines[start_y]) if char == "S"])

size_y = len(lines)
size_x = len(lines[0])
distance_array = -np.ones([size_y, size_x]).astype(int)
distance_array[start_y, start_x] = 0

pipes = {
    "|": ("N", "S"),
    "-": ("E", "W"),
    "L": ("N", "E"),
    "J": ("N", "W"),
    "7": ("S", "W"),
    "F": ("S", "E"),
    "S": ("N", "S", "E", "W"),
    ".": (),
}

step_indices = {
    "N": (-1, 0),
    "S": (1, 0),
    "E": (0, 1),
    "W": (0, -1),
}

opposite = {
    "N": "S",
    "S": "N",
    "E": "W",
    "W": "E",
}


def new_distance(distance_array):
    keepgoing = False
    current_max = np.max(distance_array)
    pos_y, pos_x = np.where(distance_array == current_max)
    for y, x in zip(pos_y, pos_x):
        symbol = lines[y][x]
        for direction in pipes[symbol]:
            y_step, x_step = step_indices[direction]
            new_y = y + y_step
            new_x = x + x_step
            if distance_array[new_y, new_x] == -1:
                distance_array[new_y, new_x] = current_max + 1
                keepgoing = True
                print(distance_array)
    return distance_array, keepgoing


for direction in ["N", "S", "E", "W"]:
    y_step, x_step = step_indices[direction]
    new_y = start_y + y_step
    new_x = start_x + x_step
    if 0 <= new_y < size_y and 0 <= new_x < size_x:
        print(opposite[direction])
        print(pipes[lines[new_y][new_x]])
        if opposite[direction] in pipes[lines[new_y][new_x]]:
            distance_array[new_y, new_x] = 1

done = False
while not done:
    done = True
    current_max = np.max(distance_array)
    pos_y, pos_x = np.where(distance_array == current_max)
    for y, x in zip(pos_y, pos_x):
        symbol = lines[y][x]
        for direction in pipes[symbol]:
            y_step, x_step = step_indices[direction]
            new_y = y + y_step
            new_x = x + x_step
            if (
                0 <= new_y < size_y and 0 <= new_x < size_x
            ):  # check for allowed position
                if opposite[direction] in pipes[lines[new_y][new_x]]:
                    if distance_array[new_y, new_x] == -1:
                        distance_array[new_y, new_x] = distance_array[y, x] + 1
                        done = False

plt.imshow(distance_array)
plt.colorbar()
plt.show()
print(np.max(distance_array))
