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
    prevSeen = {
        "rows": { num: {} for num in range(len(board)) },
        "columns": { num: {} for num in range(len(board[0])) }
    }
    buckets = [[{} for _ in range(3)] for _ in range(3)]
    
    for y in range(len(board)):
        for x in range(len(board[y])):
            currentNum = board[y][x]
            
            if (currentNum == "."):
                continue
            
            if currentNum in prevSeen["rows"][y]:
                return False
            if currentNum in prevSeen["columns"][x]:
                return False
            
            prevSeen["rows"][y][currentNum] = True
            prevSeen["columns"][x][currentNum] = True
                            
            bucketY = y // 3
            bucketX = x // 3
            
            if currentNum in buckets[bucketY][bucketX]:
                return False
            
            buckets[bucketY][bucketX][currentNum] = True
            
    return True