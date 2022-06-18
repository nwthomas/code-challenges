"""
https://leetcode.com/problems/game-of-life/

According to Wikipedia's article: "The Game of Life, also known simply as Life, is a cellular automaton devised by the British mathematician John Horton Conway in 1970."

The board is made up of an m x n grid of cells, where each cell has an initial state: live (represented by a 1) or dead (represented by a 0). Each cell interacts with its eight neighbors (horizontal, vertical, diagonal) using the following four rules (taken from the above Wikipedia article):

Any live cell with fewer than two live neighbors dies as if caused by under-population.
Any live cell with two or three live neighbors lives on to the next generation.
Any live cell with more than three live neighbors dies, as if by over-population.
Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
The next state is created by applying the above rules simultaneously to every cell in the current state, where births and deaths occur simultaneously. Given the current state of the m x n grid board, return the next state.

Example 1:
Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]

Example 2:
Input: board = [[1,1],[1,0]]
Output: [[1,1],[1,1]]

Constraints:
m == board.length
n == board[i].length
1 <= m, n <= 25
board[i][j] is 0 or 1.
"""

from typing import List

def game_of_life(board: List[List[int]]) -> None:
    """Takes in a game of life game 2D matrix and modifies it in place with next board state"""
    for y in range(len(board)):
        for x in range(len(board[y])):
            board[y][x] = get_cell_state(board, y, x)
            
    for y in range(len(board)):
        for x in range(len(board[y])):
            board[y][x] = 1 if board[y][x] == 1 or board[y][x] == 2 else 0
    
def get_cell_state(board, y, x):
    """Takes in a board with cell coordinates and returns if should live"""
    alive = 0
    
    if y - 1 >= 0 and (board[y - 1][x] == 1 or board[y - 1][x] == 3):
        alive += 1
    if y - 1 >= 0 and x - 1 >= 0 and (board[y - 1][x - 1] == 1 or board[y - 1][x - 1] == 3):
        alive += 1
    if y - 1 >= 0 and x + 1 < len(board[y - 1]) and (board[y - 1][x + 1] == 1 or board[y - 1][x + 1] == 3):
        alive += 1
    if x - 1 >= 0 and (board[y][x - 1] == 1 or board[y][x - 1] == 3):
        alive += 1
    if x + 1 < len(board[y]) and (board [y][x + 1] == 1 or board [y][x + 1] == 3):
        alive += 1
    if y + 1 < len(board) and (board[y + 1][x] == 1 or board[y + 1][x] == 3):
        alive += 1
    if y + 1 < len(board) and x - 1 >= 0 and (board[y + 1][x - 1] == 1 or board[y + 1][x - 1] == 3):
        alive += 1
    if y + 1 < len(board) and x + 1 < len(board[y + 1]) and (board[y + 1][x + 1] == 1 or board[y + 1][x + 1] == 3):
        alive += 1

    isCellAlive = board[y][x]
    
    if isCellAlive and (alive < 2 or alive > 3):
        return 3
    elif isCellAlive:
        return 1
    elif alive == 3:
        return 2
    else:
        return 0