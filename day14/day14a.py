# We use numpy to be able to use array indexing
import numpy as np

# Load in the text, discard endlines
fname = "input"
f = open(f"day14/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

# Initialize
size_field = len(lines)
load = 0
rocks = np.array([0 for _ in lines[0]])

# For each line, check how many round rocks you encounter before running into a barrier rock
# And add the required load for these round rocks at that barrier
for line_num, line in enumerate(lines[::-1]):
    # Count round on this horizontal line
    rocks[np.where(np.array(list(line)) == "O")] += 1

    # Check for square barrier rocks
    for stop in np.where(np.array(list(line)) == "#")[0]:
        # Add the load: equal to the line number for the first 'O', one less for the second etc.
        load += sum([line_num - i for i in range(rocks[stop])])

        # Remove the counted rocks for the next barrier
        rocks[stop] = 0

# Also add the load of the round rocks that have shifted to the edge of the mirror
for stop in range(len(line)):
    load += sum([size_field - i for i in range(rocks[stop])])

# Output
print(load)
