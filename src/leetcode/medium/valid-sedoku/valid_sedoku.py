"""
Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

Each row must contain the digits 1-9 without repetition.
Each column must contain the digits 1-9 without repetition.
Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
Note:

A Sudoku board (partially filled) could be valid but is not necessarily solvable.
Only the filled cells need to be validated according to the mentioned rules.

Example 1:
Input: board =
[["5","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: true

Example 2:
Input: board =
[["8","3",".",".","7",".",".",".","."]
,["6",".",".","1","9","5",".",".","."]
,[".","9","8",".",".",".",".","6","."]
,["8",".",".",".","6",".",".",".","3"]
,["4",".",".","8",".","3",".",".","1"]
,["7",".",".",".","2",".",".",".","6"]
,[".","6",".",".",".",".","2","8","."]
,[".",".",".","4","1","9",".",".","5"]
,[".",".",".",".","8",".",".","7","9"]]
Output: false
Explanation: Same as Example 1, except with the 5 in the top left corner being modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.

Constraints:
board.length == 9
board[i].length == 9
board[i][j] is a digit 1-9 or '.'.
"""

from typing import List


def isValidSudoku(board: List[List[str]]) -> bool:
    rowToNums = {}
    columnToNums = {}
    gridToNums = {}

    for y, _ in enumerate(board):
        for x, column in enumerate(board[y]):
            # Skip "." values which aren't necessary to check
            if column == ".":
                continue

            # Set initial tracker keys if not present
            if not y in rowToNums:
                rowToNums[y] = {}
            if not x in columnToNums:
                columnToNums[x] = {}

            yGridBox = y // 3
            xGridBox = x // 3
            gridKey = f"{yGridBox}{xGridBox}"
            if gridKey not in gridToNums:
                gridToNums[gridKey] = {}

            # Perform check for num presence in sub-box grid
            if column in gridToNums[gridKey]:
                return False

            # Next, perform checks for row/column values
            if column in rowToNums[y] or column in columnToNums[x]:
                return False

            # Set values in trackers for later comparisons
            rowToNums[y][column] = True
            columnToNums[x][column] = True
            gridToNums[gridKey][column] = True

    return True
