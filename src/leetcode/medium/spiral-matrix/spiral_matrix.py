"""
https://leetcode.com/problems/spiral-matrix/

Given an m x n matrix, return all elements of the matrix in spiral order.

Example 1:

Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [1,2,3,6,9,8,7,4,5]

Example 2:

Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
Output: [1,2,3,4,8,12,11,10,9,5,6,7]

Constraints:

m == matrix.length
n == matrix[i].length
1 <= m, n <= 10
-100 <= matrix[i][j] <= 100
"""

from typing import List

def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
    result = [matrix[0][0]]
    tracker = set()
    tracker.add((0, 0))
    direction = "down" if len(matrix[0]) == 1 else "right"
    y, x = 0, 0
    
    while True:
        if direction == "right" and x + 1 < len(matrix[0]) and (y, x + 1) not in tracker:
            x += 1
            result.append(matrix[y][x])
            tracker.add((y, x))
            
            if x + 1 >= len(matrix[0]) or (y, x + 1) in tracker:
                direction = "down"
                
        elif direction == "down" and y + 1 < len(matrix) and (y + 1, x) not in tracker:
            y += 1
            result.append(matrix[y][x])
            tracker.add((y, x))
            
            if y + 1 >= len(matrix) or (y + 1, x) in tracker:
                direction = "left"
                
        elif direction == "left" and x - 1 >= 0 and (y, x - 1) not in tracker:
            x -= 1
            result.append(matrix[y][x])
            tracker.add((y, x))
        
            if x - 1 < 0 or (y, x - 1) in tracker:
                direction = "up"
                
        elif direction == "up" and y - 1 >= 0 and (y - 1, x) not in tracker:
            y -= 1
            result.append(matrix[y][x])
            tracker.add((y, x))
            
            if y - 1 < 0 or (y - 1, x) in tracker:
                direction = "right"

        else:
            break

    return result