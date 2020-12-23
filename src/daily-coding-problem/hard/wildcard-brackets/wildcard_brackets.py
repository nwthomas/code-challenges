"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

You're given a string consisting solely of (, ), and *. * can represent either a (, ), or an empty string. Determine whether the parentheses are balanced.

For example, (()* and (*) are balanced. )*( is not balanced.
"""

def is_balanced_parentheses_string(string):
    """Takes in a string of ), (, and *, and determines if it's a balanced set"""
    if type(string) != str:
        raise TypeError("The argument for is_balanced_parentheses_string must be of type string.")

    if len(string) <= 0:
        return False

    opposites = {
        "(": [")", "*"],
        ")": ["(", "*"],
        "*": ["(", ")", "*"],
    }
    tracker_list = []

    for char in string:
        if char not in opposites:
            return False
        elif len(tracker_list) >= 1 and tracker_list[len(tracker_list) - 1] in opposites[char]:
            tracker_list.pop()
        else:
            tracker_list.append(char)
    
    return len(tracker_list) <= 0
