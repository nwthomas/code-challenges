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

from sortedcontainers import SortedDict


class Solution:
    def group_anagrams(self, strs: List[str]) -> List[List[str]]:
        groups = {}

        for s in strs:
            key = self.convert_str_to_deterministic_key(s)

            if key not in groups:
                groups[key] = [s]
            else:
                groups[key].append(s)

        return list(groups.values())

    def convert_str_to_deterministic_key(self, unsorted_str: str) -> str:
        result = ""
        tracker = SortedDict()

        for s in unsorted_str:
            if not s in tracker:
                tracker[s] = 1
            else:
                tracker[s] += 1

            for key in tracker.keys():
                if tracker[key] > 1:
                    for _ in range(tracker[key]):
                        result += key
                else:
                    result += key

            return result
