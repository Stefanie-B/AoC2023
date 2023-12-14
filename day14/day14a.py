# We use numpy to be able to use array indexing
import numpy as np

# Load in the text, discard endlines
fname = "input"
f = open(f"day14/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

size_field = len(lines)
weight = 0
rocks = np.array([0 for _ in lines[0]])
for line_num, line in enumerate(lines[::-1]):
    rocks[np.where(np.array(list(line)) == "O")] += 1
    for stop in np.where(np.array(list(line)) == "#")[0]:
        weight += sum([line_num - i for i in range(rocks[stop])])
        rocks[stop] = 0

for stop in range(len(line)):
    weight += sum([size_field - i for i in range(rocks[stop])])

print(weight)

"""
size_field = len(lines)
stops = [[size_field + 1] for _ in lines[0]]
rocks = [[] for _ in lines[0]]
for line_number, line in enumerate(lines):
    [
        rocks[char_number].append(size_field - line_number)
        for char_number, char in enumerate(list(line))
        if char == "O"
    ]
    [
        stops[char_number].append(size_field - line_number)
        for char_number, char in enumerate(list(line))
        if char == "#"
    ]

for col_number, stop in enumerate(stops):
    print(rocks[col_number] < stop)
"""
