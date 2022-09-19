"""
https://leetcode.com/problems/unique-paths-ii

You are given an m x n integer array grid. There is a robot initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m-1][n-1]). The robot can only move either down or right at any point in time.

An obstacle and space are marked as 1 or 0 respectively in grid. A path that the robot takes cannot include any square that is an obstacle.

Return the number of possible unique paths that the robot can take to reach the bottom-right corner.

The testcases are generated so that the answer will be less than or equal to 2 * 109.

Example 1:
Input: obstacleGrid = [[0,0,0],[0,1,0],[0,0,0]]
Output: 2
Explanation: There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

Example 2:
Input: obstacleGrid = [[0,1],[0,0]]
Output: 1

Constraints:
m == obstacleGrid.length
n == obstacleGrid[i].length
1 <= m, n <= 100
obstacleGrid[i][j] is 0 or 1.
"""

from typing import List

def unique_paths_with_obstacles(obstacle_grid: List[List[int]]) -> int:
    cache = {}
    cache[(0, 0)] = 1
    
    for y in range(len(obstacle_grid)):
        for x in range(len(obstacle_grid[y])):
            if obstacle_grid[y][x] == 1:
                cache[(y, x)] = 0
                continue
                
            current_total_ways = 0
                
            if (y - 1, x) in cache:
                current_total_ways += cache[(y - 1, x)]
            if (y, x - 1) in cache:
                current_total_ways += cache[(y, x - 1)]
            if not (y, x) in cache:
                cache[(y, x)] = 0
                
            cache[(y, x)] = max(cache[(y, x)], current_total_ways)
            
    return cache[(len(obstacle_grid) - 1, len(obstacle_grid[0]) - 1)]