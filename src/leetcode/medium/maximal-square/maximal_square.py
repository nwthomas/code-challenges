"""
https://leetcode.com/problems/maximal-square

Given an m x n binary matrix filled with 0's and 1's, find the largest square containing only 1's and return its area.

Example 1:
Input: matrix = [["1","0","1","0","0"],["1","0","1","1","1"],["1","1","1","1","1"],["1","0","0","1","0"]]
Output: 4

Example 2:
Input: matrix = [["0","1"],["1","0"]]
Output: 1

Example 3:
Input: matrix = [["0"]]
Output: 0

Constraints:
m == matrix.length
n == matrix[i].length
1 <= m, n <= 300
matrix[i][j] is '0' or '1'.
"""

from copy import deepcopy
from typing import List

def maximal_square(matrix: List[List[str]]) -> int:
    dp = deepcopy(matrix)
    dp.insert(0, [0] * len(matrix[0]))
    dp = [[0] + l for l in dp]
    longest_width = 0
    
    for y in range(1, len(dp)):
        for x in range(1, len(dp[y])):
            current = int(dp[y][x])
            min_surrounding = min(int(dp[y - 1][x]), int(dp[y - 1][x - 1]), int(dp[y][x - 1]))
            
            if current == 1 and min_surrounding > 0:
                dp[y][x] = min_surrounding + 1
            
            longest_width = max(longest_width, int(dp[y][x]))
    
    return longest_width ** 2 if longest_width > 1 else longest_width