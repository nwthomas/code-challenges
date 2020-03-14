"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Bloomberg.

Determine whether there exists a one-to-one character mapping from one string s1 to another s2.

For example, given s1 = abc and s2 = bcd, return true since we can map a to b, b to c, and c to d.

Given s1 = foo and s2 = bar, return false since the o cannot map to two characters.
"""


def are_strings_mappable(s1, s2):
    """
    Takes in two strings and evaluates if a direct mapping relationship is possible

    Returns True if possible or False otherwise
    """
    if type(s1) != str or type(s2) != str:
        raise TypeError("Arguments of are_strings_mappable must be a string")
    if len(s1) != len(s2):
        return False

    tracker = {}

    for i in range(0, len(s1)):
        if s2[i] in tracker:
            if tracker[s2[i]] != s1[i]:
                return False
            else:
                continue
        else:
            tracker[s2[i]] = s1[i]

    return True
