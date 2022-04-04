"""
Given two strings, determine if they share a common substring. A substring may be as small as one character.

Example
s1 = "and"
s1 = "art"

These share the common substring a.

s1 = "be"
s2 = "cat"

These do not share a substring.

Function Description

Complete the function twoStrings in the editor below.

twoStrings has the following parameter(s):
- string s1: a string
- string s2: another string

Returns

- string: either YES or NO
"""

def do_two_strings_share_substrings(s1, s2):
    """Take in two strings and detect if they share any substring in common"""
    left_index = 0
    right_index = len(s1) - 1

    while left_index < right_index:
        if s2.find(s1[left_index]) > -1 or s2.find(s1[right_index]) > -1:
            return True
        
        left_index += 1
        right_index -= 1

    return False