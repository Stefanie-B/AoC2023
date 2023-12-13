# We use numpy to be able to use array indexing
import numpy as np

# Load in the text, discard endlines
fname = "input"
f = open(f"day13/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()


def split_patterns(lines):
    patterns = []

    this_pattern = []
    for line_num, line in enumerate(lines):
        if line == "":
            patterns.append(np.array(this_pattern))
            this_pattern = []
        else:
            this_pattern.append([char == "#" for char in line])
    patterns.append(np.array(this_pattern))
    return patterns


def check_one_reflection(pattern, line_number):
    if line_number <= pattern.shape[0] // 2:
        pattern1 = pattern[:line_number, :]
        pattern2 = pattern[line_number : 2 * line_number, :]
    else:
        pattern2 = pattern[line_number:, :]
        pattern1 = pattern[line_number - pattern2.shape[0] : line_number, :]

    return np.sum((pattern1 != pattern2[::-1, :])) == 1


def find_horizontal_reflection(pattern):
    for rownumber in range(1, pattern.shape[0]):
        if check_one_reflection(pattern, rownumber):
            return rownumber
    return 0


def value_of_pattern(pattern):
    axis = find_horizontal_reflection(pattern) * 100
    if axis != 0:
        return axis
    return find_horizontal_reflection(pattern.T)


patterns = split_patterns(lines)
print(sum([value_of_pattern(pattern) for pattern in patterns]))
