"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a string of words delimited by spaces, reverse the words in string. For example, given "hello world here", return "here world hello"
"""


def reverse_words(string):
    """
    Reverses a space-delimited string of words using the string and list methods
    """
    if type(string) is not str:
        return None
    str_list = string.split(" ")
    str_list.reverse()
    reversed_str = " ".join(str_list)
    return reversed_str
