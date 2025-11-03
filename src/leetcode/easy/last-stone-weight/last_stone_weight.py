"""
https://leetcode.com/problems/last-stone-weight/description/

You are given an array of integers stones where stones[i] represents the weight of the ith stone.

We want to run a simulation on the stones as follows:
- At each step we choose the two heaviest stones, with weight x and y and smash them togethers
- If x == y, both stones are destroyed
- If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
- If x < y, the stone of weight x is destroyed, and the stone of weight y has new weight y - x.
- Continue the simulation until there is no more than one stone remaining.
- Return the weight of the last remaining stone or return 0 if none remain.

Example 1:
Input: stones = [2,3,6,2,4]
Output: 1
Explanation:
We smash 6 and 4 and are left with a 2, so the array becomes [2,3,2,2].
We smash 3 and 2 and are left with a 1, so the array becomes [1,2,2].
We smash 2 and 2, so the array becomes [1].

Example 2:
Input: stones = [1,2]
Output: 1

Constraints:
1 <= stones.length <= 20
1 <= stones[i] <= 100
"""

from heapq import heappush, heappop
from typing import List

def last_stone_weight(stones: List[int]) -> int:
    h = []
    for s in stones:
        heappush(h, s * -1)
    
    while len(h) > 0:
        current_one = heappop(h) * -1
        current_two = heappop(h) * -1 if len(h) > 0 else None

        if current_one and current_two is None or current_one is None and current_two:
            return current_one if not None else current_two

        if current_one == current_two:
            continue
        
        current_difference = max(current_one, current_two) - min(current_one, current_two)
        heappush(h, current_difference * -1)

    return 0
