"""
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

Example
s = mom

The list of all anagrammatic pairs is [m,m], [mo,om] at positions [[0], [2]], [[0,1], [1,2]] respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below.

sherlockAndAnagrams has the following parameter(s):

- string s: a string

Returns

- int: the number of unordered anagrammatic pairs of substrings in 
"""

# Main function
def sherlock_and_anagrams(s):
    """Returns the total count of anagrams found within the string"""
    substrings = get_all_substrings(s)
    total_anagrams = 0

    for i in range(len(substrings)):
        total_anagrams += count_anagrams(i, substrings)

    return total_anagrams

# Utility functions
def count_anagrams(current_index, substrings):
    """Finds all anagrams of the current substring within substrings array"""
    current_substring = substrings[current_index]
    rest_substrings = substrings[current_index + 1:]
    anagram_count = 0

    for i in range(len(rest_substrings)):
        if len(current_substring) == len(rest_substrings[i]) and are_anagrams(current_substring, rest_substrings[i]):
            anagram_count += 1

    return anagram_count

def are_anagrams(s1, s2):
    """Takes in two strings and returns true if anagrams and false if not"""
    tracker = {}

    for i in range(len(s1)):
        if not s1[i] in tracker:
            tracker[s1[i]] = 0

        tracker[s1[i]] += 1

    for i in range(len(s2)):
        if s2[i] in tracker and tracker[s2[i]] != 0:
            tracker[s2[1]] -= 1
        else:
            return False

    return True


def get_all_substrings(s):
    """Takes in a string and returns all substring permutations"""
    substrings = []

    for i in range(len(s)):
        for j in range(len(s)):
            substrings.append(s[i, j])

    return substrings

