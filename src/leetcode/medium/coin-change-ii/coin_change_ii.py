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

from typing import List, Type

def change(amount: int, coins: List[int]) -> int:
    if type(amount) != int:
        raise TypeError("First argument of change must be of type int")
    if type(coins) != list:
        raise TypeError("Second argument of change must be of type list")

    dp =[[0 if i > 0 else 1 for i in range(amount + 1)] for _ in coins]
    
    for row, coin in enumerate(coins):
        if type(coin) != int:
            raise TypeError("Values in second argument of change must be of type int")

        for slot in range(1, len(dp[row])):
            prev_slot = slot - coin
            
            if prev_slot >= 0:
                dp[row][slot] = dp[row][prev_slot]
            if row > 0:
                dp[row][slot] += dp[row - 1][slot]
                
    return dp[len(coins) - 1][amount]