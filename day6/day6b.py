import numpy as np


# Input
fname = "input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

time = int("".join([i for i in lines[0] if i.isdigit()]))
record = int("".join([i for i in lines[1] if i.isdigit()])) + 1

determinants = time**2 - 4 * record
first_time = np.ceil((time - np.sqrt(determinants)) / 2).astype(int)
last_time = np.floor((time + np.sqrt(determinants)) / 2).astype(int)
number_of_times = last_time - first_time + 1

print(np.prod(number_of_times))
