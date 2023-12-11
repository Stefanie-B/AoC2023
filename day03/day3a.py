# We will need numpy for arrays
import numpy as np

# Input
fname = "input"
f = open(f"day03/{fname}.txt", "r")
lines = f.readlines()
f.close()

# Create an array for non-period characters and for digits
chars = np.zeros([len(lines), len(lines[0]) - 1]).astype(bool)
digits = np.zeros([len(lines), len(lines[0]) - 1]).astype(bool)
for start_pos, line in enumerate(lines):
    # For the digits, we select using isdigit(), for the chars, we simply exclude periods and digits
    digits[start_pos, :] = [line[_].isdigit() for _ in range(len(lines[0]) - 1)]
    chars[start_pos, :] = [line[_] != "." for _ in range(len(lines[0]) - 1)]
chars[digits] = False

# Select all pixels around a char as an extension of that char. We can use + here as or because this
# is a boolean array
extended = chars.copy()
extended[:, :-1] += chars[:, 1:]
extended[:, 1:] += chars[:, :-1]
extended[:-1, :] += chars[1:, :]
extended[1:, :] += chars[:-1, :]
extended[:-1, :-1] += chars[1:, 1:]
extended[1:, 1:] += chars[:-1, :-1]
extended[:-1, 1:] += chars[1:, :-1]
extended[1:, :-1] += chars[:-1, 1:]

# Select all the digit positions
digitposx, digitposy = np.where(digits)

# We walk through all digit positions, select the full length of the digits and check whether
# they overlap with the area around a char
total = 0
start_pos = 0
while start_pos < len(digitposx):
    end_pos = start_pos
    # See if the next digit is still part of the same number (x pos or line should remain the same
    # and the y pos or index in the line should go up by one at a time, gaps in this pattern
    # mean that we reach a new number. Update the ending position of the line accordingly
    try:
        while (digitposx[end_pos] == digitposx[start_pos]) and (
            digitposy[end_pos + 1] == digitposy[end_pos] + 1
        ):
            end_pos += 1
    # Used to catch the end of the array
    except:
        IndexError

    # We check if any of the pixels within the number also overlap with a True in the extended
    # character array, which selects 'squares' around the characters
    if any(extended[digitposx[start_pos], digitposy[start_pos : end_pos + 1]]):
        # Convert the separate digits to a number
        digits = lines[digitposx[start_pos]][
            digitposy[start_pos] : digitposy[end_pos] + 1
        ]
        total += int(digits)

    # Select the next number
    start_pos = end_pos + 1

print(total)
