"""
https://leetcode.com/problems/group-anagrams

Given an array of strings strs, group the
anagrams together. You can return the answer in any order.

Example 1:
Input: strs = ["eat","tea","tan","ate","nat","bat"]
Output: [["bat"],["nat","tan"],["ate","eat","tea"]]

Explanation:
There is no string in strs that can be rearranged to form "bat".
The strings "nat" and "tan" are anagrams as they can be rearranged to form each other.
The strings "ate", "eat", and "tea" are anagrams as they can be rearranged to form each other.

Example 2:
Input: strs = [""]
Output: [[""]]

Example 3:
Input: strs = ["a"]
Output: [["a"]]

Constraints:
1 <= strs.length <= 104
0 <= strs[i].length <= 100
strs[i] consists of lowercase English letters.
"""
from typing import List


def group_anagrams(strs: List[str]) -> List[List[str]]:
    tracker = {}

    for new_str in strs:
        key = {}
        for char in new_str:
            if not char in key:
                key[char] = 0
            key[char] += 1

        sorted_key = tuple(sorted(key.items()))
        if not sorted_key in tracker:
            tracker[sorted_key] = []
        tracker[sorted_key].append(new_str)

    return list(tracker.values())
