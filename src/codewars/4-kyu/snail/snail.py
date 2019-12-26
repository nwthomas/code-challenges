"""
https://www.codewars.com/kata/snail/python

Snail Sort
Given an n x n array, return the array elements arranged from outermost elements to the middle element, traveling clockwise.

array = [[1,2,3],
         [4,5,6],
         [7,8,9]]
snail(array) #=> [1,2,3,6,9,8,7,4,5]
For better understanding, please follow the numbers of the next array consecutively:

array = [[1,2,3],
         [8,9,4],
         [7,6,5]]
snail(array) #=> [1,2,3,4,5,6,7,8,9]

__________
_______  |
|  ___|  |
|________|

NOTE: The idea is not sort the elements from the lowest value to the highest; the idea is to traverse the 2-d array in a clockwise snailshell pattern.

NOTE 2: The 0x0 (empty matrix) is represented as en empty array inside an array [[]].
"""


def snail(list):
    path = []
    x = 0
    y = 0
    dir = "r"
    directions = {"r": "d", "d": "l", "l": "t", "t": "r"}
    visited = set()
    for _ in range(0, len(list) * len(list[0])):
        path.append(list[x][y])
        visited.add((x, y))
        if dir == "r":
            if y + 1 >= len(list[0]) or (x, y + 1) in visited:
                dir = directions[dir]
                x += 1
            else:
                y += 1
        elif dir == "d":
            if x + 1 >= len(list) or (x + 1, y) in visited:
                dir = directions[dir]
                y -= 1
            else:
                x += 1
        elif dir == "l":
            if y - 1 < 0 or (x, y - 1) in visited:
                dir = directions[dir]
                x -= 1
            else:
                y -= 1
        else:
            if x - 1 < 0 or (x - 1, y) in visited:
                dir = directions[dir]
                y += 1
            else:
                x -= 1
    return path
