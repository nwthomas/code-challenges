"""
Write a function that takes a 2D binary array and returns the number of 1 islands.
An island consists of 1s that are connected to the north, south, east, or west.

For example:

islands = [[0, 1, 0, 1, 0],
           [1, 1, 0, 1, 1],
           [0, 0, 1, 0, 0],
           [1, 0, 1, 0, 0],
           [1, 1, 0, 0, 0]]

island_counter(islands) # returns 4
"""


def island_counter(islands):
    """
    Iterates through a 2D matrix to find all islands of connecting 1s
    """
    if len(islands) <= 0:
        return 0
    if type(islands) is not list or type(islands[0]) is not list:
        return None
    visited = set()
    total_islands = 0

    def check_for_island(x, y):
        """
        Visits a specific value to see if its value is 1 and, if it is, visits
        surrounding north, south, east, west values to see if they're part of
        the same island
        """
        if (x, y) in visited:
            return None
        else:
            visited.add((x, y))
            if islands[x][y] == 1:
                if x - 1 >= 0:
                    check_for_island(x - 1, y)
                if x + 1 < len(islands):
                    check_for_island(x + 1, y)
                if y - 1 >= 0:
                    check_for_island(x, y - 1)
                if y + 1 < len(islands[x]):
                    check_for_island(x, y + 1)
                return True
            else:
                return False

    for x in range(0, len(islands)):
        for y in range(0, len(islands[x])):
            if (x, y) in visited:
                continue
            else:
                result = check_for_island(x, y)
                if result:
                    total_islands += 1

    return total_islands
