"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a stack of N elements, interleave the first half of the stack with the second half reversed using only one other queue. This should be done in-place.

Recall that you can only push or pop from a stack, and enqueue or dequeue from a queue.

For example, if the stack is [1, 2, 3, 4, 5], it should become [1, 5, 2, 4, 3]. If the stack is [1, 2, 3, 4], it should become [1, 4, 2, 3].

Hint: Try working backwards from the end state.
"""


def interleave_two_lists(num_list):
    """
    Takes in a list of numbers and interleaves them with the second half reversed
    """

    if type(num_list) != list:
        raise TypeError("The argument for interleave_two_lists must be a list")

    if len(num_list) <= 2:
        return num_list

    final_list = []
    left = 0
    right = len(num_list) - 1

    for _ in range(0, len(num_list) // 2):
        final_list.append(num_list[left])
        final_list.append(num_list[right])
        left += 1
        right -= 1

    return final_list
