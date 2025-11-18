"""
https://leetcode.com/problems/coin-change-ii/

You are given an integer array coins representing coins of different denominations and an integer amount representing a total amount of money.

Return the number of combinations that make up that amount. If that amount of money cannot be made up by any combination of the coins, return 0.

You may assume that you have an infinite number of each kind of coin.

The answer is guaranteed to fit into a signed 32-bit integer.

Example 1:
Input: amount = 5, coins = [1,2,5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Example 2:
Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Example 3:
Input: amount = 10, coins = [10]
Output: 1

Constraints:
1 <= coins.length <= 300
1 <= coins[i] <= 5000
All the values of coins are unique.
0 <= amount <= 5000
"""

from typing import List

def changeIterative(amount: int, coins: List[int]) -> int:
    cache = [0 for _ in range(amount + 1)]
    cache[0] = 1

    for c in range(len(coins) - 1, -1, -1):
        for a in range(1, amount + 1):
            cache[a] += cache[a - coins[c]] if coins[c] <= a else 0

    return cache[amount]

def changeRecursive(amount: int, coins: List[int]) -> int:
    cache = {}

    def dfs(i, a):
        nonlocal cache
        if a == amount:
            return 1
        if a > amount or i == len(coins):
            return 0
        if (i, a) in cache:
            return cache[(i, a)]
        
        cache[(i, a)] = dfs(i, a + coins[i]) + dfs(i + 1, a)
        return cache[(i, a)]

    return dfs(0, 0)
