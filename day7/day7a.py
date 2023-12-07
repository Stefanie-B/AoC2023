import numpy as np

cardvals = {"T": 8, "J": 9, "Q": 10, "K": 11, "A": 12}
for i in range(2, 10):
    cardvals[str(i)] = i - 2

print(cardvals)


class Hand:
    def __init__(self, inputline):
        cards, bid = inputline.strip(" \n").split(" ")
        self.bid = int(bid)
        self.cards = list(cards)

    def classify(self):
        self.cards = np.array(self.cards)
        num_incommon = np.max([sum(self.cards == self.cards[i]) for i in range(5)])
        if num_incommon == 1:  # high card
            print(self.cards, "high card")
            return
        elif num_incommon == 2:  # one pair or two pair
            num_unique = len(np.unique(self.cards))
            if num_unique == 4:  # one pair
                self.value += 1 * 13**5
                print(self.cards, "one pair")
            else:  # two pair
                self.value += 2 * 13**5
                print(self.cards, "two pair")
        elif num_incommon == 3:  # three of a kind or full house
            num_unique = len(np.unique(self.cards))
            if num_unique == 3:  # three of a kind
                self.value += 3 * 13**5
                print(self.cards, "three of a kind")
            else:  # full house
                self.value += 4 * 13**5
                print(self.cards, "full house")
        else:  # four of a kind or five of a hind
            print(num_incommon)
            self.value += (num_incommon + 1) * 13**5
            print(self.cards, "four/five of a kind")

    def card_worth(self):
        self.value = sum(
            [
                cardvals[card] * (13 ** (4 - cardnum))
                for cardnum, card in enumerate(self.cards)
            ]
        )
        # print(self.value)

    def compute_value(self):
        self.card_worth()
        self.classify()
        return self.value


# Input
fname = "input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

hands = [Hand(i) for i in lines]
values = [hand.compute_value() for hand in hands]
indices = np.argsort(
    a=values,
)

# [setattr(hand, "rank", indices[i] + 1) for i, hand in enumerate(hands)]
scores = [(i + 1) * hands[ind].bid for i, ind in enumerate(indices)]
print(sum(scores))
