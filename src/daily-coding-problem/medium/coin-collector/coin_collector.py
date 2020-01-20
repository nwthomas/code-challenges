"""
Good morning! Here's your coding interview problem for today.

This question was asked by Zillow.

You are given a 2-d matrix where each cell represents number of coins in that cell. Assuming we start at matrix[0][0], and can only move right or down, find the maximum number of coins you can collect by the bottom right corner.

For example, in this matrix

0 3 1 1
2 0 0 4
1 5 3 1
The most we can collect is 0 + 2 + 1 + 5 + 3 + 1 = 12 coins.
"""


def find_most_coins_path(matrix):
    """
    Takes in a 2D matrix and returns the path (either right or down for each move, exclusively)
    that sums up to the most coins
    """
    if type(matrix) != list or len(matrix) <= 0:
        return None

    def find_coin_path(matrix_2d, x=0, y=0):
        if x == len(matrix_2d) - 1 and y == len(matrix_2d[0]) - 1:
            return matrix_2d[x][y]
        else:
            right = None
            down = None
            if x + 1 < len(matrix_2d):
                right = matrix_2d[x][y] + find_coin_path(matrix_2d, x + 1, y)
            if y + 1 < len(matrix[0]):
                down = matrix_2d[x][y] + find_coin_path(matrix_2d, x, y + 1)
            if right and down:
                return right if right > down else down
            elif type(right) is int:
                return right
            elif type(down) is int:
                return down

    result = find_coin_path(matrix)

    return result
