fname = "input"

# list to store a number in for each line
numbers = []
f = open(f"{fname}.txt", "r")
for x in f.readlines():
    digits = []
    for char in x:
        # If char is a number, we append it to the list
        if char.isdigit():
            digits.append(int(char))
    # The number of a line consists of the first and last digits
    new_number = digits[0] * 10 + digits[-1]
    numbers.append(new_number)
f.close()
# output
print(sum(numbers))
