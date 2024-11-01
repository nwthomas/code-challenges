"""
https://leetcode.com/problems/min-cost-climbing-stairs

You are given an integer array cost where cost[i] is the cost of ith step on a staircase. Once you pay the cost, you can either climb one or two steps.

You can either start from the step with index 0, or the step with index 1.

Return the minimum cost to reach the top of the floor.

Example 1:

Input: cost = [10,15,20]
Output: 15
Explanation: You will start at index 1.
- Pay 15 and climb two steps to reach the top.
The total cost is 15.

Example 2:

Input: cost = [1,100,1,1,1,100,1,1,100,1]
Output: 6
Explanation: You will start at index 0.
- Pay 1 and climb two steps to reach index 2.
- Pay 1 and climb two steps to reach index 4.
- Pay 1 and climb two steps to reach index 6.
- Pay 1 and climb one step to reach index 7.
- Pay 1 and climb two steps to reach index 9.
- Pay 1 and climb one step to reach the top.
The total cost is 6.

Constraints:

2 <= cost.length <= 1000
0 <= cost[i] <= 999
"""
from typing import List


def get_min_cost_climbing_stairs(cost: List[int]) -> int:
    """Returns the minimum cost to climb a set of stairs starting at either 0 or 1 step"""
    if len(cost) <= 1:
        return 0 if len(cost) < 1 else cost[0]

    last_step = len(cost) - 1
    cache = {last_step: cost[last_step]}

    def climb(step):
        if step in cache:
            return cache[step]
        elif step > len(cost) - 1:
            return 0

        current_total = cost[step]

        one_step = climb(step + 1)
        two_step = climb(step + 2)
        cache[step] = current_total + min(one_step, two_step)

        return cache[step]

    climb(0)
    min_cost = cache[0] if cache[0] < cache[1] else cache[1]

    return min_cost
