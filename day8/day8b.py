import numpy as np


class Node:
    def __init__(self, line) -> None:
        halves = line.split(", ")
        self.left = halves[0][-3:]
        self.right = halves[1][:3]
        self.name = line.split(" =")[0]
        self.paths = {}

    def calc_subpath(self, node_dict, count):
        start_count = count
        next_step = self.name
        while (not next_step.endswith("Z")) or count == start_count:
            instruction = instructions[count % len(instructions)]
            count += 1
            if instruction == "L":
                next_step = node_dict[next_step].left
            elif instruction == "R":
                next_step = node_dict[next_step].right
            else:
                raise ValueError("You're reading the instructions wrong")
        self.paths[start_count] = (count - start_count, next_step)


node_dict = {}

# Input
fname = "input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

instructions = lines[0].strip("\n")

current_nodes = []
counts = []
for linenum, line in enumerate(lines[2:]):
    node = Node(line)
    node_dict[node.name] = node
    if node.name.endswith("A"):
        current_nodes.append(node.name)
        counts.append(0)

# print(len(instructions))
node_dict[current_nodes[0]].calc_subpath(node_dict, counts[0] % len(instructions))
counts[0], current_nodes[0] = node_dict[current_nodes[0]].paths[counts[0]]
while sum([count != counts[0] for count in counts]) > 0:
    index = np.argmin(counts)
    normalized_count = counts[index] % len(instructions)
    this_node = node_dict[current_nodes[index]]
    if normalized_count not in this_node.paths.keys():
        this_node.calc_subpath(node_dict, normalized_count)
    distance, new_node = this_node.paths[normalized_count]
    counts[index] += distance
    node_dict[current_nodes[index]] = this_node
    current_nodes[index] = new_node
    # print(counts, node_dict[current_nodes[index]].paths)
print(counts[0])

"""
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

print(count)"""
