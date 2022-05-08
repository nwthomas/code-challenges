"""
https://leetcode.com/problems/two-sum/

Given an array of integers, return indices of the two numbers such that they add up to a specific target.

You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:
Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].
"""

def two_sum(nums, target):
    """
    :type nums: List[int]
    :type target: int
    :rtype: List[int]
    """
    tracker = {}
    
    for i, val in enumerate(nums):
        diff = target - val
        
        if diff in tracker:
            larger = i if nums[i] >= nums[tracker[diff]] else tracker[diff]
            smaller = tracker[diff] if nums[i] >= nums[tracker[diff]] else i
            
            return [smaller, larger]
        else:
            tracker[val] = i

    return []
