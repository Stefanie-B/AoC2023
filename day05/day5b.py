# Needed for array indexing
import numpy as np


def lookup_in_block(mappable, length_of_range, map):
    """
    Map an output number to an input number using the numbers given in a block.

    Parameters
    ----------
    mappable : int
        Output number to be converted to an output number
    length_of_range : int
        Indicates how large the range of mappables is that also follows this path without splits
        such that if <loc2> = <loc1 + n>, then <seed1> = <seed2 + n>
    map : np.ndarray of int
        List of numbers that map the ouput number to an input number

    Returns
    -------
    int
        Input number
    """
    maplength = map.shape[0]
    alternative_range = length_of_range
    for i in range(maplength):
        # For each line, we check if the output is in an output range given by its start and length
        # If this is the case, the output is equal to the input plus the difference between the
        # start of the output range and the start of the input range
        if map[i, 0] <= mappable < map[i, 0] + map[i, 2]:
            startval = mappable - map[i, 0] + map[i, 1]

            # We also calculate how large the range behind this output is that follows the same path.
            # For this we need to consider the range of numbers within this block that follow the
            # same path, and check whether it is smaller than the old range
            length_of_range = np.min(
                [length_of_range, map[i, 1] + map[i, 2] - startval]
            )

            # We can now return the mapping
            return startval, length_of_range

        # If we didn't find a mapping, the output number is equal to the input number. We do need to
        # keep in mind that the range may change, so we create an 'alternative range' which we shorten
        # to the distance between the start of the input range and the output number
        elif map[i, 0] > mappable and alternative_range > map[i, 0] - mappable:
            alternative_range = map[i, 0] - mappable
    return mappable, alternative_range


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

# Read in the seed starts and ranges
seed_starts = [int(line) for line in lines[0].strip("seeds: \n").split(" ")[::2]]
seed_ranges = [int(line) for line in lines[0].strip("seeds: \n").split(" ")[1::2]]

# For each location number starting at 0, we will try to see if it maps to a seed within the
# given intervals. We also record the range of the interval which will follow a same path
# such that if <loc2> = <loc1 + n>, then <seed1> = <seed2 + n>, so that we can skip those
# locations and don't need to follow the same path twice
startcoord = 0
length_of_range = np.infty
done = False
while not done:
    coord = startcoord

    # Check the full mapping from location to seed and for what range this mapping is valid
    for block_no in range(block_count)[::-1]:
        coord, length_of_range = lookup_in_block(
            coord, length_of_range, infoblocks[block_no]
        )

    # Check whether the found seed range coincides with with the ranges given in the input file
    for i in range(len(seed_starts)):
        if seed_starts[i] <= coord < seed_starts[i] + seed_ranges[i]:
            # Output the first element in the valid range
            print(startcoord)
            done = True

    # Skip ahead past the full range of locations that follow the same map
    startcoord += length_of_range
