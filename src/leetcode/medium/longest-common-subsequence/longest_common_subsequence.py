"""
https://leetcode.com/problems/longest-common-subsequence/

Given two strings text1 and text2, return the length of their longest common subsequence. If
there is no common subsequence, return 0.

A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

For example, "ace" is a subsequence of "abcde".
A common subsequence of two strings is a subsequence that is common to both strings.

Example 1:
Input: text1 = "abcde", text2 = "ace" 
Output: 3  
Explanation: The longest common subsequence is "ace" and its length is 3.

Example 2:
Input: text1 = "abc", text2 = "abc"
Output: 3
Explanation: The longest common subsequence is "abc" and its length is 3.

Example 3:
Input: text1 = "abc", text2 = "def"
Output: 0
Explanation: There is no such common subsequence, so the result is 0.

Constraints:
1 <= text1.length, text2.length <= 1000
text1 and text2 consist of only lowercase English characters.
"""


def get_longest_common_subsequence(text1: str, text2: str) -> int:
    """Returns the longest common subsequence between two strings"""
    grid = [[0 for _ in range(len(text2) + 1)] for _ in range(len(text1) + 1)]

    for y in range(len(text1) - 1, -1, -1):
        for x in range(len(text2) - 1, -1, -1):
            if text1[y] == text2[x]:
                grid[y][x] = 1 + grid[y + 1][x + 1]
            else:
                grid[y][x] = max(grid[y + 1][x], grid[y][x + 1])

    return grid[0][0]
