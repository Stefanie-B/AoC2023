# Input
fname = "input"
f = open(f"day04/{fname}.txt", "r")
lines = f.readlines()
f.close()

# The scores are 0-->0, 1-->1, 2-->2, 3-->4, 4-->8, we just create a dict following the series
# so we don't need to recompute this. I should probably set the number in the map to the number
# of numbers per card, but I was lazy and used 11 as that was the first value that didn't give
# me a key error
score_table = {0: 0}
for i in range(1, 11):
    score_table[i] = 2 ** (i - 1)

# This list keeps track of how many copies of each game card we have. In hindsight it is a bit
# overkill, since you only need to keep track of the next few cards and throwing out past cards
number_of_cards = {}
for i in range(len(lines)):
    number_of_cards[i] = 1

for cardnumber, line in enumerate(lines):
    # Remove the name of the card
    game, all_nums = line.strip("\n").split(":")

    # split into the winning numbers and the playing numbers and parse the numbers to integers
    winning_nums, play_nums = all_nums.split("|")
    winning_nums = [int(i) for i in winning_nums.split(" ") if i != ""]
    play_nums = [int(i) for i in play_nums.split(" ") if i != ""]

    # Check how many playing numbers are winning numbers
    wins = sum([play_num in winning_nums for play_num in play_nums])

    # For the next number of cards equal to #wins, add a number of cards equal to the number
    # of copies of the current card
    for i in range(wins):
        if cardnumber + i + 1 < len(lines):  # Only use existing game numbers
            number_of_cards[cardnumber + i + 1] += number_of_cards[cardnumber]

# Output the total number of cards
print(sum(list(number_of_cards.values())))
