"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Goldman Sachs.

You are given N identical eggs and access to a building with k floors. Your task is to find the lowest floor that will cause an egg to break, if dropped from that floor. Once an egg breaks, it cannot be dropped again. If an egg breaks when dropped from the xth floor, you can assume it will also break when dropped from any floor greater than x.

Write an algorithm that finds the minimum number of trial drops it will take, in the worst case, to identify this floor.

For example, if N = 1 and k = 5, we will need to try dropping the egg at every floor, beginning with the first, until we reach the fifth floor, so our solution will be 5.
"""

def get_egg_broken_floor(n: int, k: int) -> int:
    dp = [[0] * (k + 1) for _ in range(n + 1)]

    # Base case for only 1 egg
    for j in range(1, k + 1):
        dp[1][j] = j

    # Base case for 
    for i in range(1, n + 1):
        dp[i][0] = 0
        dp[i][1] = 1

    return dp[n][k]