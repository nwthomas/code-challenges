"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Square.

A competitive runner would like to create a route that starts and ends at his house, with the condition that the route goes entirely uphill at first, and then entirely downhill.

Given a dictionary of places of the form {location: elevation}, and a dictionary mapping paths between some of these locations to their corresponding distances, find the length of the shortest route satisfying the condition above. Assume the runner's home is location 0.

For example, suppose you are given the following input:

elevations = {0: 5, 1: 25, 2: 15, 3: 20, 4: 10}
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

def find_shortest_route(elevations, paths):
    if dict.keys(elevations) <= 0 or dict.keys(paths) <= 0:
        return None
    if type(elevations) != dict or type(paths) != dict:
        raise TypeError("The arguments for find_shortest_route must be of type dict.")

    tracker = [("0", key[1], paths[key]) for key in dict.keys(paths) if key[0] == 0]
    visited = set()
    final = None

    while len(tracker) > 0:
        current_tuple = tracker.pop()
        path, current_location, current_elevation = current_tuple

        if current_location == 0:
            final_tuple = (f"{path} -> 0", current_elevation)
            if not final:
                final = final_tuple
            elif final[1] > current_elevation:
                final = final_tuple
            continue

        for key in paths:
            if key[0] == current_location and key not in visited:
                tracker.append((f"{path} -> {current_location}", key[1], current_elevation + paths[key]))
    
    return final


