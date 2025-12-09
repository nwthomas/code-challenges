"""
https://leetcode.com/problems/walls-and-gates

You are given a m × n 2D grid initialized with these three possible values:
-1 - A water cell that can not be traversed.
0 - A treasure chest.
INF - A land cell that can be traversed. We use the integer 2^31 - 1 = 2147483647 to represent INF.

Fill each land cell with the distance to its nearest treasure chest. If a land cell cannot reach a treasure chest then the value should remain INF.

Assume the grid can only be traversed up, down, left, or right.

Modify the grid in-place.

Example 1:
Input: [
  [2147483647,-1,0,2147483647],
  [2147483647,2147483647,2147483647,-1],
  [2147483647,-1,2147483647,-1],
  [0,-1,2147483647,2147483647]
]
Output: [
  [3,-1,0,1],
  [2,2,1,-1],
  [1,-1,2,-1],
  [0,-1,3,4]
]

Example 2:
Input: [
  [0,-1],
  [2147483647,2147483647]
]
Output: [
  [0,-1],
  [1,2]
]

Constraints:
m == grid.length
n == grid[i].length
1 <= m, n <= 100
grid[i][j] is one of {-1, 0, 2147483647}
"""

from typing import List


def wallsAndGrapes(grid: List[List[int]]) -> None:
    chests = []

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 0:
                chests.append([y, x])

    def dfs(y: int, x: int, distance: int):
        if grid[y][x] == -1 or grid[y][x] == 0:
            return
        if grid[y][x] < distance:
            return

        grid[y][x] = distance
        newDistance = distance + 1

        helper(y, x, newDistance)

    def helper(y: int, x: int, distance: int):
        if x - 1 >= 0:
            dfs(y, x - 1, distance)
        if x + 1 < len(grid[y]):
            dfs(y, x + 1, distance)
        if y - 1 >= 0:
            dfs(y - 1, x, distance)
        if y + 1 < len(grid):
            dfs(y + 1, x, distance)

    for chest in chests:
        y, x = chest
        helper(y, x, 1)
