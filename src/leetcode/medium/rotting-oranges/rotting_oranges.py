"""
https://leetcode.com/problems/rotting-oranges/

You are given a 2-D matrix grid. Each cell can have one of three possible values:

0 representing an empty cell
1 representing a fresh fruit
2 representing a rotten fruit
Every minute, if a fresh fruit is horizontally or vertically adjacent to a rotten fruit, then the fresh fruit also becomes rotten.

Return the minimum number of minutes that must elapse until there are zero fresh fruits remaining. If this state is impossible within the grid, return -1.

Example 1:
Input: grid = [[1,1,0],[0,1,1],[0,1,2]]
Output: 4

Example 2:
Input: grid = [[1,0,1],[0,2,0],[1,0,1]]
Output: -1

Constraints:
1 <= grid.length, grid[i].length <= 10
"""


def getOrangesToInfect(grid: list[list[int]], y: int, x: int) -> list[list[int]]:
    oranges = []

    if y > 0 and grid[y - 1][x] == 1:
        oranges.append([y - 1, x])
    if y < len(grid) - 1 and grid[y + 1][x] == 1:
        oranges.append([y + 1, x])
    if x > 0 and grid[y][x - 1] == 1:
        oranges.append([y, x - 1])
    if x < len(grid[y]) - 1 and grid[y][x + 1] == 1:
        oranges.append([y, x + 1])

    return oranges


def orangesRotting(grid: list[list[int]]) -> int:
    rotten = {}
    minutes = 0

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 2 and len(getOrangesToInfect(grid, y, x)) > 0:
                rotten[f"{y},{x}"] = [y, x]

    while len(rotten.keys()) > 0:
        updatedRotten = {}
        for key in rotten.keys():
            y, x = rotten[key]
            possibleInfections = getOrangesToInfect(grid, y, x)

            for infection in possibleInfections:
                grid[infection[0]][infection[1]] = 2
                if len(getOrangesToInfect(grid, infection[0], infection[1])) > 0:
                    updatedRotten[f"{infection[0]},{infection[0]}"] = [
                        infection[0],
                        infection[1],
                    ]

        rotten = updatedRotten
        minutes += 1

    for y in range(len(grid)):
        for x in range(len(grid[y])):
            if grid[y][x] == 1:
                return -1

    return minutes
