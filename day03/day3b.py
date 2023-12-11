# We will need numpy for arrays
import numpy as np

# Input
fname = "input"
f = open(f"day03/{fname}.txt", "r")
lines = f.readlines()
f.close()

# Create an array for the stars and digits and read them in
xsize = len(lines)
ysize = len(lines[0]) - 1
stars = np.zeros([xsize, ysize]).astype(bool)
digits = np.zeros([xsize, ysize]).astype(bool)
for start_pos, line in enumerate(lines):
    digits[start_pos, :] = [line[_].isdigit() for _ in range(len(lines[0]) - 1)]
    stars[start_pos, :] = [line[_] == "*" for _ in range(len(lines[0]) - 1)]

# We walk through all star positions, and for each star walk through the digits, to check if
# two border the star
starposx, starposy = np.where(stars)
digitposx, digitposy = np.where(digits)
total = 0
for start_pos in range(len(starposx)):
    # Select the square around a star to compare the digit positions to
    x = starposx[start_pos]
    y = starposy[start_pos]
    starrange = np.zeros(stars.shape)
    starrange[
        (x - 1) % xsize : (x + 2) % (xsize + 1), (y - 1) % ysize : (y + 2) % (ysize + 1)
    ] = True

    # Walk through the digits
    start_pos = 0
    numbers = []
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
        except IndexError:  # Used to catch the end of the array
            pass

        # If the number overlaps with a square around a star, append the number to the list
        if any(starrange[digitposx[start_pos], digitposy[start_pos : end_pos + 1]]):
            number = lines[digitposx[start_pos]][
                digitposy[start_pos] : digitposy[end_pos] + 1
            ]
            numbers.append(int(number))

        # Go to next number
        start_pos = end_pos + 1

    # If more than one number borders the star, take the product of the numbers and add them to
    # the output
    if len(numbers) > 1:
        ratio = np.prod(np.array(numbers))
        total += ratio
print(total)
