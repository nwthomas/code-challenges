"""
https://leetcode.com/problems/surrounded-regions/description

You are given a 2-D matrix board containing 'X' and 'O' characters.

If a continous, four-directionally connected group of 'O's is surrounded by 'X's, it is considered to be surrounded.

Change all surrounded regions of 'O's to 'X's and do so in-place by modifying the input board.

Example 1:
Input: board = [
  ["X","X","X","X"],
  ["X","O","O","X"],
  ["X","O","O","X"],
  ["X","X","X","O"]
]
Output: [
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","X"],
  ["X","X","X","O"]
]

Explanation: Note that regions that are on the border are not considered surrounded regions.

Constraints:
1 <= board.length, board[i].length <= 200
board[i][j] is 'X' or 'O'.
"""


def traverse(board, y: int, x: int, seen: dict) -> bool:
    if y < 0 or y > len(board) - 1:
        return False
    if x < 0 or x > len(board[y]) - 1:
        return False
    if (y, x) in seen:
        return True
    if board[y][x] == "X":
        return True

    seen.add((y, x))

    results = [
        traverse(board, y - 1, x, seen),
        traverse(board, y + 1, x, seen),
        traverse(board, y, x - 1, seen),
        traverse(board, y, x + 1, seen),
    ]

    for r in results:
        if not r:
            return False

    return True


def fill_cells(board, y: int, x: int):
    if board[y][x] == "X":
        return

    board[y][x] = "X"

    fill_cells(board, y - 1, x)
    fill_cells(board, y + 1, x)
    fill_cells(board, y, x - 1)
    fill_cells(board, y, x + 1)


def surroundRegions(board: list[list[str]]) -> None:
    for y in range(len(board)):
        for x in range(len(board[y])):
            if board[y][x] == "O" and traverse(board, y, x, set()):
                fill_cells(board, y, x)

    return board
