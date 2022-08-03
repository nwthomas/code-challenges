"""
https://leetcode.com/problems/number-of-islands

Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water), return the number of islands.

An island is surrounded by water and is formed by connecting adjacent lands horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.

Example 1:
Input: grid = [
  ["1","1","1","1","0"],
  ["1","1","0","1","0"],
  ["1","1","0","0","0"],
  ["0","0","0","0","0"]
]
Output: 1

Example 2:
Input: grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]
Output: 3

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 300
grid[i][j] is '0' or '1'.
"""

from typing import List, Type

def num_islands(grid: List[List[str]]) -> int:
    if type(grid) != list:
        raise TypeError("Argument must be of type lists within list")

    total_islands = 0
    cache = {}
    
    def traverse(y, x):
        if (y, x) in cache or grid[y][x] == "0":
            return
        else:
            cache[(y, x)] = True
            
            if y - 1 >= 0:
                traverse(y - 1, x)
            if x - 1 >= 0:
                traverse(y, x - 1)
            if y + 1 < len(grid):
                traverse(y + 1, x)
            if x + 1 < len(grid[y]):
                traverse(y, x + 1)
                
    for y in range(len(grid)):
        if type (grid[y]) != list:
            raise TypeError("Argument must be of type lists within list")

        for x in range(len(grid[y])):
            if type(grid[y][x]) != str:
                raise TypeError("Cells within grid must be of type string")
                
            if (y, x) not in cache and grid[y][x] == "1":
                total_islands += 1
                traverse(y, x)
                
    return total_islands