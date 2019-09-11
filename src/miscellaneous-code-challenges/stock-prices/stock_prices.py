"""
You want to write a bot that will automate the task of day-trading for you while you're going through Lambda. You decide to have your bot just focus on buying and selling Amazon stock.

Write a function `find_max_profit` that receives as input a list of stock prices. Your function should return the maximum profit that can be made from a single buy and sell. You must buy first before selling; no shorting is allowed here.

For example, `find_max_profit([1050, 270, 1540, 3800, 2])` should return 3530, which is the maximum profit that can be made from a single buy and then sell of these stock prices.

For this problem, we essentially want to find the maximum difference between the smallest and largest prices in the list of prices, but we also have to make sure that the max profit is computed by subtracting some price by another price that comes _before_ it; it can't come after it in the list of prices.

So what if we kept track of the `current_min_price_so_far` and the `max_profit_so_far`?

Run the test file by executing `python test_stock_prices.py`.

You can also test your implementation manually by executing `python stock_prices.py [integers_separated_by_a_single_space]`
"""

import argparse


def find_max_profit(prices):
    if len(prices) <= 1:
        return None
    prior_smallest = prices[0]
    max_profit_so_far = prices[1] - prior_smallest
    for i in range(1, len(prices) - 1):
        new_profit = prices[i] - prior_smallest
        if new_profit > max_profit_so_far:
            max_profit_so_far = new_profit
        if prices[i] < prior_smallest:
            prior_smallest = prices[i]
    return max_profit_so_far


if __name__ == '__main__':
    parser = argparse.ArgumentParser(
        description='Find max profit from prices.')
    parser.add_argument('integers', metavar='N', type=int,
                        nargs='+', help='an integer price')
    args = parser.parse_args()

    print("A profit of ${profit} can be made from the stock prices {prices}.".format(
        profit=find_max_profit(args.integers), prices=args.integers))
