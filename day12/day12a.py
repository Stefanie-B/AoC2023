# We use numpy to be able to use array indexing
import numpy as np

# Load in the text, discard endlines
fname = "input"
f = open(f"day12/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()


def read_complete_map(map):
    lengthlist = []
    startchar = 0
    for charnum, char in enumerate(map):
        if char == ".":
            if charnum != startchar:
                lengthlist.append(charnum - startchar)
            startchar = charnum + 1
    if charnum + 1 != startchar:
        lengthlist.append(charnum + 1 - startchar)
    return lengthlist


def build_string(incomplete_map, positions_unknown, number_unknown, num_positive):
    bitstring = f"{num_positive:0100b}"[::-1]
    bitstring = bitstring.replace("0", ".")
    complete_map = np.array(list(incomplete_map))
    complete_map[positions_unknown] = list(bitstring[:number_unknown])
    return "".join(complete_map)


def number_per_map(line):
    incomplete_map, counts = line.split(" ")
    counts = [int(i) for i in counts.split(",")]

    number_possible = 0
    number_unknown = 0
    positions_unknown = []
    for pos, char in enumerate(incomplete_map):
        if char == "?":
            positions_unknown.append(pos)
            number_unknown += 1
    # print(number_unknown, incomplete_map)
    for map_number in range(2**number_unknown):
        new_map = build_string(
            incomplete_map, positions_unknown, number_unknown, map_number
        )
        counts_new_map = read_complete_map(new_map)
        # print(new_map, counts_new_map)
        if counts == counts_new_map:
            number_possible += 1
    return number_possible


total = 0
for linenum, line in enumerate(lines):
    print(linenum, total)
    total += number_per_map(line)

print(total)
