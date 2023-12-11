# We use numpy to be able to use array indexing
import numpy as np

# Load in the text, discard endlines
fname = "input"
f = open(f"day09/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()

# We walk through the lines
total = 0
for line in lines:
    # Split the string into its separate numbers
    numbers = np.array(line.split(" ")).astype(int)

    # The extrapolated value only depends on the first values of the difference strings. That
    # is all we need to record
    first_values = []
    while sum(abs(numbers)) != 0:
        first_values.append(numbers[0])
        numbers = np.diff(numbers)

    # The extrapolated value is equal to (-1)^n x_n for n=0 to where all differences are zero
    # This is because we always subtract the extrapolated value at the current level from the
    # first difference value at the previous level, such that the sign flips with each level you
    # go up
    extrapolated_value = sum(first_values[::2]) - sum(first_values[1::2])

    # Record the output
    total += extrapolated_value
print(total)
