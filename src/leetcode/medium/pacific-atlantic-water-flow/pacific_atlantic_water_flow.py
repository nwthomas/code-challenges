"""
https://leetcode.com/problems/pacific-atlantic-water-flow

There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.

Example 1:
Input: heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
Output: [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]

Example 2:
Input: heights = [[2,1],[1,2]]
Output: [[0,0],[0,1],[1,0],[1,1]]

Constraints:
m == heights.length
n == heights[r].length
1 <= m, n <= 200
0 <= heights[r][c] <= 105
"""

from typing import List

def pacific_atlantic(heights: List[List[int]]) -> List[List[int]]:
    cache = {}
    output = []
    
    def traverse(y, x, from_pacific, prev_value):
        if heights[y][x] < prev_value:
            return
        if (y, x) in cache and from_pacific and cache[(y, x)]["pacific"]:
            return
        if (y, x) in cache and not from_pacific and cache[(y, x)]["atlantic"]:
            return
            
        if not (y, x) in cache:
            cache[(y, x)] = { "pacific": False, "atlantic": False }
            
        if from_pacific:
            cache[(y, x)]["pacific"] = True
        else:
            cache[(y, x)]["atlantic"] = True
            
        if y + 1 < len(heights):
            traverse(y + 1, x, from_pacific, heights[y][x])
        if x + 1 < len(heights[y]):
            traverse(y, x + 1, from_pacific, heights[y][x])
        if y - 1 >= 0:
            traverse(y - 1, x, from_pacific, heights[y][x])
        if x - 1 >= 0:
            traverse(y, x - 1, from_pacific, heights[y][x])
                
    for y in range(len(heights)):
        traverse(y, 0, True, heights[y][0])
        traverse(y, len(heights[y]) - 1, False, heights[y][len(heights[y]) - 1])
        
    for x in range(len(heights[0])):
        traverse(0, x, True, heights[0][x])
        traverse(len(heights) - 1, x, False, heights[len(heights) - 1][x])
        
    for y in range(len(heights)):
        for x in range(len(heights[y])):
            if (y, x) in cache:
                current = cache[(y, x)]

                if current["pacific"] and current['atlantic']:
                    output.append([y, x])
                
    return output