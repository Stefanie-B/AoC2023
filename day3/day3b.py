import numpy as np

fname = "input"


f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

xsize = len(lines)
ysize = len(lines[0]) - 1
stars = np.zeros([xsize, ysize]).astype(bool)
digits = np.zeros([xsize, ysize]).astype(bool)

for i, line in enumerate(lines):
    digits[i, :] = [line[_].isdigit() for _ in range(len(lines[0]) - 1)]
    stars[i, :] = [line[_] == "*" for _ in range(len(lines[0]) - 1)]


starposx, starposy = np.where(stars)
digitposx, digitposy = np.where(digits)
total = 0
for i in range(len(starposx)):
    x = starposx[i]
    y = starposy[i]

    starrange = np.zeros(stars.shape)
    starrange[
        (x - 1) % xsize : (x + 2) % (xsize + 1), (y - 1) % ysize : (y + 2) % (ysize + 1)
    ] = True

    i = 0
    numbers = []
    while i < len(digitposx):
        j = i
        try:
            while (digitposx[j] == digitposx[i]) and (
                digitposy[j + 1] == digitposy[j] + 1
            ):
                j += 1
        except IndexError:
            continue

        if any(starrange[digitposx[i], digitposy[i : j + 1]]):
            number = int(lines[digitposx[i]][digitposy[i] : digitposy[j] + 1])
            numbers.append(number)

        i += 1
        i = j + 1

    if len(numbers) > 1:
        ratio = np.prod(np.array(numbers))
        total += ratio
print(total)
