import numpy as np


def lookup_in_block(mappable, end_of_range, map):
    maplength = map.shape[0]
    others_range = end_of_range
    for i in range(maplength):
        if map[i, 0] <= mappable < map[i, 0] + map[i, 2]:
            startval = mappable - map[i, 0] + map[i, 1]
            end_of_range = np.min([end_of_range, map[i, 1] + map[i, 2] - startval])
            return startval, end_of_range
        elif map[i, 0] > mappable and others_range > map[i, 0] - mappable:
            others_range = map[i, 0] - mappable
    return mappable, others_range


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

seed_starts = [int(line) for line in lines[0].strip("seeds: \n").split(" ")[::2]]
seed_ranges = [int(line) for line in lines[0].strip("seeds: \n").split(" ")[1::2]]

startcoord = 0
end_of_range = np.infty
while True:
    coord = startcoord
    for block_no in range(block_count)[::-1]:
        coord, end_of_range = lookup_in_block(coord, end_of_range, infoblocks[block_no])

    for i in range(len(seed_starts)):
        if seed_starts[i] <= coord < seed_starts[i] + seed_ranges[i]:
            print(startcoord)
            raise ValueError
    print(startcoord, coord, end_of_range)
    startcoord += end_of_range
