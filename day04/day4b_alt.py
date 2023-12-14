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

# This list keeps track of how many copies of the next few game cards we have
number_of_cards = []

score = 0
for cardnumber, line in enumerate(lines):
    # Remove the name of the card
    game, all_nums = line.strip("\n").split(":")

    # split into the winning numbers and the playing numbers and parse the numbers to integers
    winning_nums, play_nums = all_nums.split("|")
    winning_nums = [int(i) for i in winning_nums.split(" ") if i != ""]
    play_nums = [int(i) for i in play_nums.split(" ") if i != ""]

    # Check how many playing numbers are winning numbers
    wins = sum([play_num in winning_nums for play_num in play_nums])

    # We pop the current card from the stack to check how many we have and at this number to the score
    # if we didn't win any new cards, the card won't be in the stack so we simply have a single
    # card
    if len(number_of_cards) > 0:
        copies_this_card = number_of_cards.pop(0)
    else:
        copies_this_card = 1
    score += copies_this_card

    # Add the won cards to the stack. If the card wasn't in the stack yet, we add 1 (original card) +
    # the cards we just won, otherwise we simply add the won cards
    for i in range(wins):
        if i >= len(number_of_cards):
            number_of_cards.append(copies_this_card + 1)
        else:
            number_of_cards[i] += copies_this_card


# Output the total number of cards
print(score)
