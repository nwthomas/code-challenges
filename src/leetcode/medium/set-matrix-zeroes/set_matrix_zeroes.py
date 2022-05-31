"""
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.

Example 1:
Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output: [[1,0,1],[0,0,0],[1,0,1]]

Example 2:
Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]

Constraints:
m == matrix.length
n == matrix[0].length
1 <= m, n <= 200
-231 <= matrix[i][j] <= 231 - 1
"""

from typing import List

def set_zeroes(matrix: List[List[int]]) -> None:
    """Takes in a 2D matrix and modifies it in place to set all rows/columns of a 0 to also 0"""
    tracker = []
    
    def flipToZeroes(y, x):
        y1, y2 = y, y
        x1, x2 = x, x
        
        while -1 < y1 or y2 < len(matrix) or -1 < x1 or x2 < len(matrix[y]):
            if -1 < y1:
                matrix[y1][x] = 0
                y1 -= 1
            if y2 < len(matrix):
                matrix[y2][x] = 0
                y2 += 1
            if -1 < x1:
                matrix[y][x1] = 0
                x1 -= 1
            if x2 < len(matrix[0]):
                matrix[y][x2] = 0
                x2 += 1
                
    for y in range(len(matrix)):
        for x in range(len(matrix[0])):
            if matrix[y][x] == 0:
                tracker.append([y, x])
                
    while len(tracker) > 0:
        y, x = tracker.pop()
        flipToZeroes(y, x)