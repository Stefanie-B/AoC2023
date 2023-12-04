import numpy as np

fname = "input"


f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

score_table = {0: 0}
for i in range(1, 11):
    score_table[i] = 2 ** (i - 1)

number_of_cards = {}
for i in range(len(lines)):
    number_of_cards[i] = 1

for cardnumber, line in enumerate(lines):
    game, all_nums = line.strip("\n").split(":")
    winning_nums, game_nums = all_nums.split("|")
    winning_nums = [int(i) for i in winning_nums.split(" ") if i != ""]
    game_nums = [int(i) for i in game_nums.split(" ") if i != ""]
    wins = sum([game_num in winning_nums for game_num in game_nums])
    for i in range(wins):
        if cardnumber + i + 1 < len(lines):
            number_of_cards[cardnumber + i + 1] += number_of_cards[cardnumber]

print(sum(list(number_of_cards.values())))
