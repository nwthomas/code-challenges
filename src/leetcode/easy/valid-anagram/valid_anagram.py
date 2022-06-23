"""
https://leetcode.com/problems/valid-anagram/

Given two strings s and t, return true if t is an anagram of s, and false otherwise.

An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.

Example 1:
Input: s = "anagram", t = "nagaram"
Output: true

Example 2:
Input: s = "rat", t = "car"
Output: false

Constraints:
1 <= s.length, t.length <= 5 * 104
s and t consist of lowercase English letters.

Follow up: What if the inputs contain Unicode characters? How would you adapt your solution to such a case?
"""

def is_anagram(s: str, t: str) -> bool:
    if len(s) != len(t):
        return False
        
    s_cache = {}
    
    for char in s:
        if not char in s_cache:
            s_cache[char] = 0
            
        s_cache[char] += 1
        
    for char in t:
        if not char in s_cache:
            return False
        
        s_cache[char] -= 1
        
        if s_cache[char] == 0:
            del s_cache[char]
            
    remaining_cache_keys = dict.keys(s_cache)
    
    return len(remaining_cache_keys) == 0