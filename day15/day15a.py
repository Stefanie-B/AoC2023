# We use numpy to be able to use array indexing
import numpy as np


def parse_sequence(sequence):
    """
    Converts an input sequence using the HASH algorithm

    Parameters
    ----------
    sequence : list
        One sequence of instructions to be hashed

    Returns
    -------
    int
        Output value ocrresponding to the sequence
    """
    value = 0
    for char in sequence:
        value = ((value + ord(char)) * 17) % 256
    return value


# Load in the text, discard endlines
fname = "input"
f = open(f"day15/{fname}.txt", "r")
line = f.readlines()[0].strip("\n")
f.close()

# Parse the values and output
sequences = line.split(",")
values = sum([parse_sequence(list(sequence)) for sequence in sequences])
print(values)
