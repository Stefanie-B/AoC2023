fname = "day01/input"

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


def check_num(line, spelled_numbers):
    """
    Find the first number in a line (either spelled out or a digit)

    Parameters
    ----------
    line : str
        Line of text where numbers must be located
    spelled_numbers : list of str
        List of the spelled out numbers

    Returns
    -------
    int
        Digit corresponding to the first found number
    """
    for i, char in enumerate(line):
        # Append the numbers directly
        if char.isdigit():
            digit = int(char)
            return digit
        else:
            # check if one of the spelled out numbers starts at this character
            for j, number in enumerate(spelled_numbers):
                if line[i : i + len(number)] == number:
                    # the list is numbered 0,N-1, so j+1 is equal to the spelled out value
                    digit = j + 1
                    return digit


f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()


total = 0
for x in lines:
    # Do a forward check to find the first digit
    digit1 = check_num(x, spelled_numbers)
    # Do a backward check to find the last digit
    digit2 = check_num(x[::-1], [i[::-1] for i in spelled_numbers])
    # append the new number
    new_number = digit1 * 10 + digit2
    total += new_number

# output
print(total)
