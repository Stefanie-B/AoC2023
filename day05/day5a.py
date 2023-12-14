# Needed for array indexing
import numpy as np


def lookup_in_block(mappable, map):
    """
    Map an input number to an output number using the numbers given in a block.

    Parameters
    ----------
    mappable : int
        Input number to be converted to an output number
    map : np.ndarray of int
        List of numbers that map the input number to an output number

    Returns
    -------
    int
        Output number
    """
    maplength = map.shape[0]
    for i in range(maplength):
        # For each line, we check if the input is in an input range given by its start and length
        # If this is the case, the output is equal to the input plus the difference between the
        # start of the output range and the start of the input range
        if map[i, 1] <= mappable < map[i, 1] + map[i, 2]:
            return mappable - map[i, 1] + map[i, 0]
    # If the number doesn't correspond to any input range, we just output the original number
    return mappable


# Input
fname = "input"
f = open(f"day05/{fname}.txt", "r")
lines = f.readlines()
f.close()

# Parse the blocks
block_count = 0
infoblocks = [[]]
for line in lines[3:]:  # skip the seeds and title lines
    line = line.strip("\n")

    # If a line is empty, that means we are starting a new map-block
    if line == "":
        block_count += 1
        infoblocks.append([])
    elif not line.endswith("map:"):
        # If a line ends with "map:" it's a title block and we can throw it out
        # Otherwise, we can add the new mapping numbers to the block
        numbers = line.split(" ")
        infoblocks[block_count].append(numbers)
block_count += 1

# We convert the list of blocks to an array with integer numbers for easier indexing
for block_no in range(block_count):
    infoblocks[block_no] = np.array(infoblocks[block_no]).astype(int)

# We also parse the seed numbers
seeds = [int(line) for line in lines[0].strip("seeds: \n").split(" ")]

# We loop through the seed numbers and try to find the minimum location
min_output = np.infty
for seednumber, coord in enumerate(seeds):
    # Map the seed to a location by going through all mapping blocks
    for block_no in range(block_count):
        coord = lookup_in_block(coord, infoblocks[block_no])
    # If this location is lower than any other location, record it
    if coord < min_output:
        min_output = coord

# output
print(min_output)
