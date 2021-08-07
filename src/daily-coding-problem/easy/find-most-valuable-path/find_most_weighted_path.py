"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You are given an array of arrays of integers, where each array corresponds to a row in a triangle of numbers. For example, [[1], [2, 3], [1, 5, 1]] represents the triangle:

  1
 2 3
1 5 1
We define a path in the triangle to start at the top and go down one row at a time to an adjacent value, eventually ending with an entry on the bottom row. For example, 1 -> 3 -> 5. The weight of the path is the sum of the entries.

Write a program that returns the weight of the maximum weight path.
"""

def find_most_weighted_path_down(triangle):
    """Takes in a triangle (list of list of integers) and returns path with the most weight on the way down"""
    # Tracker stores in pattern of [total_weight, x_index, y_index]
    tracker = [[triangle[0][0], 0, 0]]
    heaviest_path = tracker[0][0]

    while len(tracker) >= 1:
      total_weight, x_index, y_index = tracker.pop()

      if x_index < len(triangle) - 1:
        x_index = x_index + 1
        y_index_one = y_index
        y_index_two = y_index + 1

        total_weight_one = total_weight + triangle[x_index][y_index_one]
        total_weight_two = total_weight + triangle[x_index][y_index_two]
        
        tracker.append([total_weight_one, x_index, y_index_one])
        tracker.append([total_weight_two, x_index, y_index_two])

      elif total_weight > heaviest_path:
        heaviest_path = total_weight

    return heaviest_path