"""
https://leetcode.com/problems/longest-substring-without-repeating-characters/

Given a string s, find the length of the longest substring without repeating characters.

Example 1:

Input: s = "abcabcbb"
Output: 3

Explanation: The answer is "abc", with the length of 3.

Example 2:

Input: s = "bbbbb"
Output: 1

Explanation: The answer is "b", with the length of 1.

Example 3:

Input: s = "pwwkew"
Output: 3

Explanation: The answer is "wke", with the length of 3.

Notice that the answer must be a substring, "pwke" is a subsequence and not a substring.

Constraints:

0 <= s.length <= 5 * 104
s consists of English letters, digits, symbols and spaces.
"""

def lengthOfLongestSubstring(s: str) -> int:
    if len(s) <= 0:
        return 0
    
    longest_substring, current_substring = 1, 1
    left, right = 0, 0
    tracker = { s[0]: 0 }
    
    while right + 1 < len(s):    
        right += 1
        char = s[right]
        
        if char not in tracker:
            tracker[char] = right
            current_substring += 1
        elif char == s[right - 1]:
            tracker[char] = right
            left = right
            current_substring = 1
        elif char in tracker and tracker[char] < left:
            tracker[char] = right
            current_substring += 1
        elif char in tracker:
            char_index = tracker[char]
            tracker[char] = right
            diff = char_index - left
            left = char_index + 1
            current_substring -= diff
            
        longest_substring = max(longest_substring, current_substring)
    
    return longest_substring