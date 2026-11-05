"""
Implement a function for the 0/1 Knapsack problem. Given a set of items, each with a weight and a value, determine the number of each item to include in a collection so that the total weight is less than or equal to a given limit and the total value is as large as possible. The solution should not exceed the knapsack's maximum capacity, C.

Your function should take as input:
A list of weights, w[i], representing the weights of each item.
A list of values, v[i], representing the value of each item.
An integer, C, representing the maximum capacity of the knapsack.
The function should return the maximum total value that can fit within the maximum capacity of the knapsack.

Examples
weights = [10, 20, 30]
values = [60, 100, 120]
capacity = 50
output: 220

weights = [1, 1, 1]
values = [10, 20, 30]
capacity = 2
output: 50

weights = [4, 2, 3]
values = [10, 20, 15]
capacity = 5
output: 35

weights = [4, 5, 1]
values = [1, 2, 3]
capacity = 4
output: 3
"""


# def knapsack(weight: list[int], values: list[int], capacity: int) -> int:
#     dp = [0 for _ in range(capacity + 1)]

#     for w in
