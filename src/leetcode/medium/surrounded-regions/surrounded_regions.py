"""
https://neetcode.io/problems/surrounded-regions/question

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


def surroundRegions(board: list[list[str]]) -> None:
    cache = {}
    toFlipCache = {}

    for y in range(len(board)):
        for x in range(len(board[y])):
            if (
                board[y][x] == "O"
                and f"{y}{x}" not in cache
                and 0 < y < len(board) - 1
                and 0 < x < len(board[0]) - 1
            ):
                responseCache = {}
                isValid = traverse(board, y, x, responseCache)
                cache = {**cache, **responseCache}
                if isValid:
                    toFlipCache = {**toFlipCache, **responseCache}

    for key in toFlipCache.keys():
        y, x = list(key)
        board[int(y)][int(x)] = "X"


def traverse(board: list[list[str]], y: int, x: int, cache: dict[str, bool]) -> bool:
    cache[f"{y}{x}"] = True

    if (y == 0 or y == len(board) - 1 or x == 0 or x == len(board[0]) - 1) and board[y][
        x
    ] == "O":
        return False

    results = []

    if y - 1 >= 0 and f"{y - 1}{x}" not in cache:
        results.append(
            True if board[y - 1][x] == "X" else traverse(board, y - 1, x, cache)
        )
    if y + 1 < len(board) and f"{y + 1}{x}" not in cache:
        results.append(
            True if board[y + 1][x] == "X" else traverse(board, y + 1, x, cache)
        )
    if x - 1 >= 0 and f"{y}{x - 1}" not in cache:
        results.append(
            True if board[y][x - 1] == "X" else traverse(board, y, x - 1, cache)
        )
    if x + 1 < len(board[0]) and f"{y}{x + 1}" not in cache:
        results.append(
            True if board[y][x + 1] == "X" else traverse(board, y, x + 1, cache)
        )

    for b in results:
        if not b:
            return False

    return True
