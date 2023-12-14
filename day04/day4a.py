# Load the input
fname = "input"
f = open(f"day04/{fname}.txt", "r")
lines = f.readlines()
f.close()

# The scores are 0-->0, 1-->1, 2-->2, 3-->4, 4-->8, we just create a dict following the series
# so we don't need to recompute this. I should probably set the number in the map to the number
# of numbers per card, but I was lazy and used 11 as that was the first value that didn't give
# me a key error
lookup_table = {0: 0}  # special case
for i in range(1, 11):
    lookup_table[i] = 2 ** (i - 1)

total = 0
for line in lines:
    # Remove the name of the card
    game, all_nums = line.strip("\n").split(":")

    # split into the winning numbers and the playing numbers and parse the numbers to integers
    winning_nums, play_nums = all_nums.split("|")
    winning_nums = [int(i) for i in winning_nums.split(" ") if i != ""]
    play_nums = [int(i) for i in play_nums.split(" ") if i != ""]

    # Check how many playing numbers are winning numbers
    wins = sum([play_num in winning_nums for play_num in play_nums])

    # Add the score for this card
    total += lookup_table[wins]

print(total)
