"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Google.

Given a word W and a string S, find all starting indices in S which are anagrams of W.

For example, given that W is "ab", and S is "abxaba", return 0, 3, and 4.
"""


def verify_string_combos(word, string):
    """
    Finds all possible indices of a word in a given string
    """
    if type(word) is not str or type(string) is not str:
        return None
    if len(word) > len(string):
        return []

    indices = []

    def isWordPresent(stringSlice):
        tracker = word[:]
        for i in range(0, len(word)):
            charIndex = tracker.find(stringSlice[i])
            if charIndex > -1:
                tracker = tracker[:charIndex] + tracker[charIndex + 1:]
            else:
                break
        return True if len(tracker) == 0 else False

    for i in range(0, len(string) - len(word) + 1):
        if word.find(string[i]) > -1:
            if len(string[i:]) >= len(word) and isWordPresent(string[i:]):
                indices.append(i)

    return indices
