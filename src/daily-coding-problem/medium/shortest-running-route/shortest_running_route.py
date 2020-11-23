"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

Given a dictionary of places of the form {location: distance}, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

In this case, the shortest valid path would be 0 -> 2 -> 4 -> 0, with a distance of 28.
"""

def find_shortest_route(paths):
    if type(paths) != dict:
        raise TypeError("The argument for find_shortest_route must be of type dict.")
    if len(dict.keys(paths)) <= 0:
        return None

    tracker = [("0", key[1], paths[key]) for key in dict.keys(paths) if key[0] == 0]
    visited = set()
    final = None

    while len(tracker) > 0:
        current_tuple = tracker.pop()
        path, current_location, current_distance = current_tuple

        if current_location == 0:
            final_tuple = (f"{path} -> 0", current_distance)
            if not final:
                final = final_tuple
            elif final[1] > current_distance:
                final = final_tuple
            continue

        for key in paths:
            if key[0] == current_location and key not in visited:
                tracker.append((f"{path} -> {current_location}", key[1], current_distance + paths[key]))
    
    return final


