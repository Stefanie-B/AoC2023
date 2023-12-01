fname = "input"

# list with all numbers spelled out
spelled_numbers = [
    "one",
    "two",
    "three",
    "four",
    "five",
    "six",
    "seven",
    "eight",
    "nine",
]

numbers = []
f = open(f"{fname}.txt", "r")
for x in f.readlines():
    digits = []
    for i, char in enumerate(x):
        # Append the numbers directly
        if char.isdigit():
            digits.append(int(char))
        else:
            # check if one of the spelled out numbers starts at this character
            for j, number in enumerate(spelled_numbers):
                if x[i : i + len(number)] == number:
                    # the list is numbered 0,N-1, so j+1 is equal to the spelled out value
                    digits.append(j + 1)
    # append the new number
    new_number = digits[0] * 10 + digits[-1]
    numbers.append(new_number)
f.close()
# output
print(sum(numbers))
