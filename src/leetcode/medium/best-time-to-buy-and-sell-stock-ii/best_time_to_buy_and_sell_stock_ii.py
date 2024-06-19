"""
https://leetcode.com/problems/best-time-to-buy-and-sell-stock-ii/description/

You are given an integer array prices where prices[i] is the price of a given stock on the ith day.

On each day, you may decide to buy and/or sell the stock. You can only hold at most one share of the
stock at any time. However, you can buy it then immediately sell it on the same day.

Find and return the maximum profit you can achieve.

 

Example 1:

Input: prices = [7,1,5,3,6,4]
Output: 7
Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
Total profit is 4 + 3 = 7.
Example 2:

Input: prices = [1,2,3,4,5]
Output: 4
Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
Total profit is 4.
Example 3:

Input: prices = [7,6,4,3,1]
Output: 0
Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the
maximum profit of 0.
"""

from typing import List


def max_profit(prices: List[int]) -> int:
    """
    Returns the maximum profit possible by buying and selling stock multiple times within a given
    period of an array of prices.
    """
    total_profit = 0

    if len(prices) <= 0:
        return total_profit

    current_profit = 0
    minimum_price = prices[0]

    for i, _ in enumerate(prices):
        current_value = prices[i]
        next_value = prices[i + 1] if i + 1 < len(prices) else None

        if next_value is not None and next_value < current_value:
            total_profit += current_profit
            current_profit = 0
            minimum_price = next_value
        elif next_value is not None:
            current_profit = next_value - minimum_price
        else:
            total_profit += current_profit

    return total_profit
