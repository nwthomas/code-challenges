"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Microsoft.

Given an array of numbers arr and a window of size k, print out the median of each window of size k starting from the left and moving right by one position each time.

For example, given the following array and k = 3:

[-1, 5, 13, 8, 2, 3, 3, 1]
Your function should print out the following:

5 <- median of [-1, 5, 13]
8 <- median of [5, 13, 8]
8 <- median of [13, 8, 2]
3 <- median of [8, 2, 3]
3 <- median of [2, 3, 3]
3 <- median of [3, 3, 1]
Recall that the median of an even-sized list is the average of the two middle numbers.
"""


def find_median_for_range(int_list, window_size):
    """Takes in a list of integers and a window size and returns the median for each window in the list"""
    isOddWindowSize = window_size % 2 != 0

    for i in range(0, len(int_list) - window_size):
        if isOddWindowSize:
            print(int_list[i + window_size // 2])
        else:
            left_index = (window_size - 1) // 2
            right_index = left_index + 1
            middle_average = (
                int_list[i + left_index] + int_list[i + right_index]) / 2
            print(middle_average)
