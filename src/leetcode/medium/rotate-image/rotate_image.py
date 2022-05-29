"""
https://leetcode.com/problems/rotate-image/

You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).

You have to rotate the image in-place, which means you have to modify the input 2D matrix directly. DO NOT allocate another 2D matrix and do the rotation.

Example 1:
Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
Output: [[7,4,1],[8,5,2],[9,6,3]]

Example 2:
Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
"""

from typing import List

def rotate(matrix: List[List[int]]) -> None:
    offset = 0
    
    def swap(y_one, x_one, y_two, x_two):
        matrix[y_one][x_one], matrix[y_two][x_two] = matrix[y_two][x_two], matrix[y_one][x_one]
    
    while offset <= len(matrix[0]) // 2:
        for i in range(len(matrix[0]) - (1 + offset * 2)):
            # Swap pivot and top right (y_one, x_one, y_two, x_two)
            swap(offset, offset + i, i + offset, len(matrix[0]) - 1 - offset)
            
            # Swap pivot and bottom right (y_one, x_one, y_two, x_two)
            swap(offset, offset + i, len(matrix[0]) - 1 - offset, len(matrix[0]) - 1 - offset - i)
            
            # Swap pivot and bottom left (y_one, x_one, y_two, x_two)
            swap(offset, offset + i, len(matrix[0]) - 1 - offset - i, 0 + offset)
            
        offset += 1
        
    return matrix