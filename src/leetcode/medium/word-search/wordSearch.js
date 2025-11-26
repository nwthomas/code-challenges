/*
https://leetcode.com/problems/word-search

Given an m x n grid of characters board and a string word, return true if word exists in the grid.

The word can be constructed from letters of sequentially adjacent cells, where adjacent cells are horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example 1:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
Output: true

Example 2:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
Output: true
Example 3:
Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
Output: false

Constraints:
m == board.length
n = board[i].length
1 <= m, n <= 6
1 <= word.length <= 15
board and word consists of only lowercase and uppercase English letters.

Follow up: Could you use search pruning to make your solution faster with a larger board?
*/

const wordSearch = (board, word) => {
    function dfs(y, x, i, cache = {}) {
        if (cache[`${y}${x}`]) {
            return false;
        }
        if (y < 0 || y > board.length - 1 || x < 0 || x > board[0].length - 1) {
            return false;
        }
        if (board[y][x] !== word[i]) {
            return false;
        }
        if (board[y][x] === word[word.length - 1] && i === word.length - 1) {
            return true;
        }

        cache[`${y}${x}`] = true;

        const results = [
            dfs(y - 1, x, i + 1, { ...cache }),
            dfs(y + 1, x, i + 1, { ...cache }),
            dfs(y, x - 1, i + 1, { ...cache }),
            dfs(y, x + 1, i + 1, { ...cache }),
        ];

        return results.some((result) => result);
    }

    for (let y = 0; y < board.length; y++) {
        for (let x = 0; x < board[y].length; x++) {
            if (board[y][x] === word[0]) {
                const result = dfs(y, x, 0);
                if (result) {
                    return true;
                }
            }
        }
    }

    return false;
};

module.exports = { wordSearch };
