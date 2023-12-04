import numpy as np

fname = "input"


f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

lookup_table = {0: 0}
for i in range(1, 11):
    lookup_table[i] = 2 ** (i - 1)

total = 0
for line in lines:
    game, all_nums = line.strip("\n").split(":")
    winning_nums, game_nums = all_nums.split("|")
    winning_nums = [int(i) for i in winning_nums.split(" ") if i != ""]
    game_nums = [int(i) for i in game_nums.split(" ") if i != ""]
    wins = sum([game_num in winning_nums for game_num in game_nums])
    total += lookup_table[wins]

print(total)
