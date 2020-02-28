"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string, return the first recurring character in it, or null if there is no recurring character.

For example, given the string "acbbac", return "b". Given the string "abcdef", return null.
"""


def find_first_recurring_char(input_string):
    """
    Takes in a string and finds the first recurring character in it
    """
    char_list = [char for char in input_string]
    tracker = set()
    for char in char_list:
        if char in tracker:
            return char
        else:
            tracker.add(char)
    return None
