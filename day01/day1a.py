# Load input
fname = "day01/input"
f = open(f"{fname}.txt", "r")
lines = f.readlines()
f.close()

# list to store a number in for each line
numbers = []
for x in lines:
    digits = []
    for char in x:
        # If char is a number, we append it to the list
        if char.isdigit():
            digits.append(int(char))
    # The number of a line consists of the first and last digits
    new_number = digits[0] * 10 + digits[-1]
    numbers.append(new_number)
# output
print(sum(numbers))
