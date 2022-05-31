"""
https://leetcode.com/problems/jump-game-ii/

Given an array of non-negative integers nums, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Your goal is to reach the last index in the minimum number of jumps.

You can assume that you can always reach the last index.

Example 1:
Input: nums = [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2. Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:
Input: nums = [2,3,0,1,4]
Output: 2

Constraints:
1 <= nums.length <= 104
0 <= nums[i] <= 1000
"""

from typing import List

def can_jump(nums: List[int]) -> int:
    jumps = 0
    l = 0
    r = 0
    
    while r < len(nums) - 1:
        farthest = 0
        
        for i in range(l, r + 1):
            new_jumps_from_here = i + nums[i]
            farthest = max(farthest, new_jumps_from_here)
            
        l = r + 1
        r = farthest
        jumps += 1
        
    return jumps