"""
https://leetcode.com/problems/word-search/

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
"""

from typing import List

def does_word_exist(board: List[List[str]], word: str) -> bool:
    if type(board) != list:
        raise TypeError("First argument for does_word_exist must be of type list")
    if type(word) != str:
        raise TypeError("Second argument for does_word_exist must be of type string")
    
    def search(y, x, index, cache):
        if index == len(word) - 1 and board[y][x] == word[index]:
            return True
        elif (y, x) in cache:
            return False
        elif board[y][x] != word[index]:
            return False
        
        cache.add((y, x))
        results = []
        
        if y - 1 >= 0 and not (y - 1, x) in cache:
            results.append(search(y - 1, x, index + 1, cache.copy()))
        if y + 1 < len(board) and not (y + 1, x) in cache:
            results.append(search(y + 1, x, index + 1, cache.copy()))
        if x - 1 >= 0 and not (y, x - 1) in cache:
            results.append(search(y, x - 1, index + 1, cache.copy()))
        if x + 1 < len(board[y]) and not (y, x + 1) in cache:
            results.append(search(y, x + 1, index + 1, cache.copy()))
            
        for result in results:
            if result:
                return True
            
        return False
    
    for y in range(len(board)):
        if type(board[y]) != list:
            raise TypeError("First argument of type list must contain only rows of type list")

        for x in range(len(board[y])):
            if type(board[y][x]) != str:
                raise TypeError("Values in lists of list must contain only type string")

            if board[y][x] == word[0]:
                result = search(y, x, 0, set())
                
                if result:
                    return True
                
    return False