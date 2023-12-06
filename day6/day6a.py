import numpy as np


# Input
fname = "input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

times = np.array([int(i) for i in lines[0].strip("\n").split(" ") if i.isdigit()])
records = np.array([int(i) for i in lines[1].strip("\n").split(" ") if i.isdigit()]) + 1

determinants = times**2 - 4 * records
first_time = np.ceil((times - np.sqrt(determinants)) / 2).astype(int)
last_time = np.floor((times + np.sqrt(determinants)) / 2).astype(int)
number_of_times = last_time - first_time + 1

print(np.prod(number_of_times))
