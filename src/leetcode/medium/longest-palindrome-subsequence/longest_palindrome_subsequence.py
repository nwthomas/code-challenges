"""
https://leetcode.com/problems/longest-palindromic-subsequence/

Given a string s, find the longest palindromic subsequence's length in s.

A subsequence is a sequence that can be derived from another sequence by deleting some or no elements without changing the order of the remaining elements.

Example 1:
Input: s = "bbbab"
Output: 4
Explanation: One possible longest palindromic subsequence is "bbbb".

Example 2:
Input: s = "cbbd"
Output: 2
Explanation: One possible longest palindromic subsequence is "bb".

Constraints:
1 <= s.length <= 1000
s consists only of lowercase English letters.
"""

def get_longest_palindrome_subsequence(s: str) -> int:
    grid = [[0 for _ in range(len(s) + 1)] for _ in range(len(s) + 1)]
    s_reversed = s[::-1]
    
    for y in range(len(s) - 1, -1, -1):
        for x in range(len(s) - 1, -1, -1):
            if s[y] == s_reversed[x]:
                grid[y][x] = 1 + grid[y + 1][x + 1]
            else:
                grid[y][x] = max(grid[y + 1][x], grid[y][x + 1])
                
    return grid[0][0]