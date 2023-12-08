import numpy as np


class Node:
    def __init__(self, line) -> None:
        halves = line.split(", ")
        self.left = halves[0][-3:]
        self.right = halves[1][:3]


node_dict = {}

# Input
fname = "input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

instructions = lines[0].strip("\n")

for linenum, line in enumerate(lines[2:]):
    node = Node(line)
    node_dict[line.split(" =")[0]] = node

next_step = "AAA"
count = 0
while next_step != "ZZZ":
    instruction = instructions[count % len(instructions)]
    count += 1
    if instruction == "L":
        next_step = node_dict[next_step].left
    elif instruction == "R":
        next_step = node_dict[next_step].right
    else:
        raise ValueError("You're reading the instructions wrong")

print(count)
