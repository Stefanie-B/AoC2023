# We use numpy to be able to use array indexing
import numpy as np


def move_column(column, end_point):
    """
    Moves the rocks up  in a column to their positions after tilting for a particular barrier
    given by the endpoint.

    Parameters
    ----------
    column : numpy ndarray of str
        column consisting of '.', 'O' and '#'
    end_point : int
        position before the rolling of rocks must stop (either the position of a '#' or -1 for the
        edge of the field)

    Returns
    -------
    column : numpy ndarray of str
        column after shifting to the specified barrier
    index : int
        index within the column of the next barrier
    """
    # This is the minimum position at which a round rock could be present
    index = end_point + 1

    # number of rocks between these barriers
    count = 0

    # move through the column until a new barrier is found, count round rocks in the process
    while column[index] != "#":
        if column[index] == "O":
            count += 1
            # Remove round rocks as we go
            column[index] = "."
        index += 1
        if index == column.size:
            break

    # place rocks in their new positions
    for rock in range(count):
        column[end_point + 1 + rock] = "O"

    # return the adjusted column and the position of the next barrier
    return column, index


def tilt_map_north(rock_map):
    """
    Tilt a full rock_map North

    Parameters
    ----------
    rock_map : numpy ndarray of str
        rock_map of square ('#') and round ('O') rocks and empty space ('.')

    Returns
    -------
    numpy ndarray of str
        rock_map of square ('#') and round ('O') rocks and empty space ('.') after tilting north
    """
    # We analyze each column separately
    for column_number in range(rock_map.shape[1]):
        column = rock_map[:, column_number]

        # The first barrier is the edge of the rock_map, so we set the position just outside the rock_map
        # as the first en _point. We then shift the rocks to each end point iteratively
        end_point = -1
        while end_point < column.size - 1:
            column, end_point = move_column(column, end_point)

        # replace the column with the shifted column
        rock_map[:, column_number] = column
    return rock_map


def perform_cycle(rock_map):
    """
    Do a full rotation cycle on a rock_map

    Parameters
    ----------
    rock_map : numpy ndarray of str
        rock_map of square ('#') and round ('O') rocks and empty space ('.')

    Returns
    -------
    numpy ndarray of str
        rock_map of square ('#') and round ('O') rocks and empty space ('.') after the rotation
    """
    # Tilt North
    rock_map = tilt_map_north(rock_map)

    # Tilt West (orient West North and tilt)
    rock_map = tilt_map_north(rock_map.T[:, ::-1])

    # Tilt South (orient South North and tilt)
    rock_map = tilt_map_north(rock_map.T)

    # Tilt East (orient East North and tilt)
    rock_map = tilt_map_north(rock_map.T[::-1, :])

    # Return the rock_map to the original orientation and return it
    return rock_map.T[::-1, ::-1]


# Load in the text, discard endlines and convert the text to an array of strings
fname = "input"
f = open(f"day14/{fname}.txt", "r")
lines = np.array([list(line.strip("\n")) for line in f.readlines()])
f.close()

# Initialize a map and the list of maps prior to the tilt cycle
max_it = 1e9
rock_map = lines
old_maps = [rock_map.copy()]
it = 1

# Perform a cycle each iteration and check whether we have found a pattern loop, if we do, we can
# skip the remaining iterations and simply select the part of the loop that will show at the final
# iteration
while it < max_it:
    # Perform a tilt cycle
    rock_map = perform_cycle(rock_map)

    # Check if this map has shown up before
    for map_number, check_map in enumerate(old_maps):
        if np.array_equal(check_map, rock_map):
            # Calculate which map will shown at the final iteration and set this at the map
            remaining_cycles = int((max_it - it) % (it - map_number))
            rock_map = old_maps[map_number + remaining_cycles]

            # Adjust to the final iteration
            it = max_it

    # append the rotated map to the list of previously shown maps and increase the iterator
    old_maps.append(rock_map.copy())
    it += 1

# Calculate the vertical positions of all round rocks and use these positions to find their loads
y_pos = np.where(rock_map == "O")[0]
loads = rock_map.shape[0] - y_pos
print(sum(loads))
