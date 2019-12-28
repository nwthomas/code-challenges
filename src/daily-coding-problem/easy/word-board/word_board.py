"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Coursera.

Given a 2D board of characters and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

For example, given the following board:

[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
exists(board, "ABCCED") returns true, exists(board, "SEE") returns true, exists(board, "ABCB") returns false.
"""


def is_word_present(board, word):
    if type(board) != list or type(board[0]) != list or type(word) != str:
        return None
    isFound = False
    root_x = 0
    root_y = 0

    def find_word(x, y, current_word=""):
        nonlocal isFound
        new_current_word = current_word + board[x][y]
        if new_current_word == word:
            isFound = True
        else:
            if new_current_word == word[:len(new_current_word)]:
                if (x + 1) < len(board):
                    find_word(x + 1, y, new_current_word)
                if (y + 1) < len(board[0]):
                    find_word(x, y + 1, new_current_word)
                if (x - 1) >= 0:
                    find_word(x - 1, y, new_current_word)
                if (y - 1) >= 0:
                    find_word(x, y - 1, new_current_word)
            else:
                return

    for _ in range(len(board) * len(board[0])):
        find_word(root_x, root_y)
        if isFound:
            break
        else:
            if root_y >= len(board[0]) - 1:
                root_y = 0
                root_x += 1
            else:
                root_y += 1

    return isFound
