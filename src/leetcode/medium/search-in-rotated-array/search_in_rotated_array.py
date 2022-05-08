"""
https://leetcode.com/problems/search-in-rotated-sorted-array/

There is an integer array nums sorted in ascending order (with distinct values).

Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

You must write an algorithm with O(log n) runtime complexity.

Example 1:

Input: nums = [4,5,6,7,0,1,2], target = 0
Output: 4
Example 2:

Input: nums = [4,5,6,7,0,1,2], target = 3
Output: -1
Example 3:

Input: nums = [1], target = 0
Output: -1

Constraints:

1 <= nums.length <= 5000
-104 <= nums[i] <= 104
All values of nums are unique.
nums is an ascending array that is possibly rotated.
-104 <= target <= 104
"""

from typing import List

def search(nums: List[int], target: int) -> int:
    if len(nums) <= 1:
        if len(nums) > 0 and nums[0] == target:
            return 0
        else:
            return -1
    
    left = 0
    right = len(nums) - 1
    
    while left < right:
        pivot = ((right - left) // 2) + left
        
        if nums[pivot] == target:
            return pivot
        elif nums[right] == target:
            return right
        elif nums[left] == target:
            return left
        
        if nums[pivot] < nums[right]:
            if target > nums[pivot] and target < nums[right]:
                left = pivot + 1
            else:
                right = pivot - 1
        else:
            if target > nums[left] and target < nums[pivot]:
                right = pivot - 1
            else:
                left = pivot + 1
            
    return -1