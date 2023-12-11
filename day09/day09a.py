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

    # The extrapolated value will be equal to the last value of each line of differences, it does not
    # matter if we include the last line of zeros in this, we just need to record all last values.
    # We can discard the old numbers and only need to keep te difference string
    last_values = []
    while sum(abs(numbers)) != 0:
        last_values.append(numbers[-1])
        numbers = np.diff(numbers)
    extrapolated_value = sum(last_values)

    # Record the output
    total += extrapolated_value
print(total)
