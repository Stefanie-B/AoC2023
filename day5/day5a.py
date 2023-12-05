import numpy as np


def lookup_in_block(mappable, map):
    maplength = map.shape[0]
    for i in range(maplength):
        if map[i, 1] <= mappable < map[i, 1] + map[i, 2]:
            return mappable - map[i, 1] + map[i, 0]
    return mappable


# Input
fname = "input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

block_count = 0
infoblocks = [[]]
for line in lines[3:]:
    line = line.strip("\n")
    if line == "":
        block_count += 1
        infoblocks.append([])
    elif not line.endswith("map:"):
        numbers = line.split(" ")
        infoblocks[block_count].append(numbers)
block_count += 1

for block_no in range(block_count):
    infoblocks[block_no] = np.array(infoblocks[block_no]).astype(int)

seeds = [int(line) for line in lines[0].strip("seeds: \n").split(" ")]

min_output = np.infty
for seednumber, coord in enumerate(seeds):
    for block_no in range(block_count):
        coord = lookup_in_block(coord, infoblocks[block_no])
    if coord < min_output:
        min_output = coord

print(min_output)
