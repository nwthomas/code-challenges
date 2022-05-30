"""
https://leetcode.com/problems/3sum/

Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.

Notice that the solution set must not contain duplicate triplets.

Example 1:
Input: nums = [-1,0,1,2,-1,-4]
Output: [[-1,-1,2],[-1,0,1]]

Example 2:
Input: nums = []
Output: []

Example 3:
Input: nums = [0]
Output: []

Constraints:
0 <= nums.length <= 3000
-105 <= nums[i] <= 105
"""

from typing import List

def three_sum(nums: List[int]) -> List[List[int]]:
    triplets = set()
    nums = sorted(nums)
    
    for i in range(0, len(nums) - 2):            
        left = i + 1
        right = len(nums) - 1
        
        while left < right:
            total = nums[i] + nums[left] + nums[right]
            
            if total == 0:
                triplets.add((nums[i], nums[left], nums[right]))
                left += 1
            elif total < 0:
                left += 1
            else:
                right -= 1
    
    return list(triplets)