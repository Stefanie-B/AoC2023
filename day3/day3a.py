import numpy as np

fname = "input"


f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

chars = np.zeros([len(lines), len(lines[0]) - 1]).astype(bool)
digits = np.zeros([len(lines), len(lines[0]) - 1]).astype(bool)

for i, line in enumerate(lines):
    digits[i, :] = [line[_].isdigit() for _ in range(len(lines[0]) - 1)]
    chars[i, :] = [line[_] != "." for _ in range(len(lines[0]) - 1)]

chars[digits] = False

extended = chars.copy()
extended[:, :-1] += chars[:, 1:]
extended[:, 1:] += chars[:, :-1]
extended[:-1, :] += chars[1:, :]
extended[1:, :] += chars[:-1, :]

extended[:-1, :-1] += chars[1:, 1:]
extended[1:, 1:] += chars[:-1, :-1]
extended[:-1, 1:] += chars[1:, :-1]
extended[1:, :-1] += chars[:-1, 1:]

digitposx, digitposy = np.where(digits)

total = 0
i = 0
while i < len(digitposx):
    j = i
    try:
        while (digitposx[j] == digitposx[i]) and (digitposy[j + 1] == digitposy[j] + 1):
            j += 1
    except:
        IndexError

    if any(extended[digitposx[i], digitposy[i : j + 1]]):
        number = int(lines[digitposx[i]][digitposy[i] : digitposy[j] + 1])
        total += number

    i += 1
    i = j + 1

print(total)
