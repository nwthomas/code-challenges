"""
Write a function that returns an array of all aanagrams of a given string. An anagram is a reordering of all characters within a string. 

For example, the anagrams of "abc" are:
[
    "abc",
    "acb",
    "bac",
    "bca",
    "cab",
    "cba"
]
"""

from typing import List
from copy import copy

def anagrams_of(string: str) -> List[str]:
    if len(string) == 1:
        return [string]

    collection = []

    substring_anagrams = anagrams_of(string[1:len(string)])

    for substring_anagram in substring_anagrams:
        for i in range(0, len(substring_anagram) + 1):
            copied_string = copy(substring_anagram)

            copied_string = copied_string[:i] + string[0] + copied_string[i:]
            collection.append(copied_string)

    return collection