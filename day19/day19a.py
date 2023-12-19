import numpy as np
from matplotlib import pyplot as plt

# Load in the text, discard endlines
fname = "input"
f = open(f"day19/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()


class Workflow:
    def __init__(self) -> None:
        pass

    def setup_workflow(self, line):
        self.name, temp = line.split("{")
        instructions = temp[:-1].split(",")
        self.evaluations = []
        self.destinations = []
        self.components = []
        for instruction in instructions[:-1]:
            self.components.append(instruction[0])
            condition, destination = instruction[1:].split(":")
            self.evaluations.append(condition)
            self.destinations.append(destination)
        # self.evaluations.append(lambda part: True)
        self.destinations.append(instructions[-1])

    def process_part(self, part):
        for evaluation, component, destination in zip(
            self.evaluations, self.components, self.destinations
        ):
            if eval(f"{part[component]}{evaluation}"):
                return destination
        return self.destinations[-1]


class Part:
    def __init__(self, line) -> None:
        properties = line[1:-1].split(",")
        self.x = int(properties[0][2:])
        self.m = int(properties[1][2:])
        self.a = int(properties[2][2:])
        self.s = int(properties[3][2:])
        self.workflow = "in"


workflows = {}
for linenum, line in enumerate(lines):
    if line == "":
        break
    workflow = Workflow()
    workflow.setup_workflow(line)
    workflows[workflow.name] = workflow

total = 0
for line in lines[linenum + 1 :]:
    properties = line[1:-1].split(",")
    part = {"workflow": "in"}
    for prop in properties:
        key, value = prop.split("=")
        part[key] = int(value)
    Part(line)
    while part["workflow"] != "A" and part["workflow"] != "R":
        this_workflow = workflows[part["workflow"]]
        part["workflow"] = this_workflow.process_part(part)
    if part["workflow"] == "A":
        total += part["x"] + part["m"] + part["a"] + part["s"]
print(total)
