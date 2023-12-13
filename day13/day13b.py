# We use numpy to be able to use array indexing
import numpy as np

# Load in the text, discard endlines
fname = "input"
f = open(f"day13/{fname}.txt", "r")
lines = [line.strip("\n") for line in f.readlines()]
f.close()


def split_patterns(lines):
    """
    Parse the input into a list of boolean arrays, such that each array represents a pattern.

    Parameters
    ----------
    lines : list of str
        input text

    Returns
    -------
    list of np.ndarrays
        List of patterns, where each pattern is represented by a boolean array which is true for
        rocks (#) and False for ash (.)
    """
    patterns = []  # List of complete patterns
    this_pattern = []  # List for current pattern under construction
    for line in lines:
        # An empty line means a pattern is finished, so we can add it to the list of patterns and
        # start a new pattern. Otherwise we simply add a new row of bools
        if line == "":
            patterns.append(np.array(this_pattern))
            this_pattern = []
        else:
            this_pattern.append([char == "#" for char in line])
    patterns.append(np.array(this_pattern))
    return patterns


def check_one_reflection(pattern, line_number):
    """
    Checks whether a single horizontal reflection would be valid when a smudge occurs

    Parameters
    ----------
    pattern : np.ndarray of bools
        Single input pattern
    line_number : int
        Number of the reflection axis (must be at least 1 and at most the height of the pattern)

    Returns
    -------
    bool
        True if the reflection is valid, False if it is not valid.
    """
    # Split the pattern into two parts: the original and the possible reflection
    # We select the 'reflected area', cutting off the part of the array that is not included in the
    # mirror (the part where one of the patterns 'sticks out')
    if line_number <= pattern.shape[0] // 2:
        pattern1 = pattern[:line_number, :]
        pattern2 = pattern[line_number : 2 * line_number, :]
    else:
        pattern2 = pattern[line_number:, :]
        pattern1 = pattern[line_number - pattern2.shape[0] : line_number, :]

    # Return True if there is a single pixel mismatch between pattern2 and pattern 1
    return np.sum((pattern1 != pattern2[::-1, :])) == 1


def find_horizontal_reflection(pattern):
    """
    Find the horizontal reflection axis of a pattern if it exists. If it does not, return 0.

    Parameters
    ----------
    pattern : np.ndarray of bools
        Single input pattern

    Returns
    -------
    int
        horizontal reflection axis if it exists, otherwise returns 0.
    """
    # At least one row must be to the left of the axis
    for rownumber in range(1, pattern.shape[0]):
        if check_one_reflection(pattern, rownumber):
            return rownumber
    # If no reflection is found, return 0
    return 0


def value_of_pattern(pattern):
    """
    Finds the 'value' of a pattern. This is equal to the reflection axis for vertical reflections,
    and 100 times the reflection axis for horizontal reflections.

    Parameters
    ----------
    pattern : np.ndarray of bools
        Single input pattern

    Returns
    -------
    int
        value of pattern
    """
    # Check the horizontal reflection and return 100 * reflection axis if it exists
    axis = find_horizontal_reflection(pattern) * 100

    # If no horizontal reflection is found, find a vertical reflection by transposing the pattern
    # and finding a horizontal reflection in the transposed pattern
    if axis == 0:
        axis = find_horizontal_reflection(pattern.T)

    return axis


# Output. Because of linearity we can sum the value per pattern rather than summing the axes first
# and then multiplying
patterns = split_patterns(lines)
print(sum([value_of_pattern(pattern) for pattern in patterns]))
