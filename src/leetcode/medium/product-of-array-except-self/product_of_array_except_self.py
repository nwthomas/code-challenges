"""
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

def product_except_self(nums: List[int]) -> List[int]:
    left_to_right = []
    right_to_left = []
    answers = []

    for i in range(len(nums)):
        num = nums[i]

        if i == 0:
            left_to_right.append(num)
        else:
            left_to_right.append(num * left_to_right[i - 1])

    for i in range(len(nums) - 1, -1, -1):
        num = nums[i]
        
        if i == len(nums) - 1:
            right_to_left.append(num)
        else:
            right_to_left.append(num * right_to_left[len(right_to_left) - 1])
    
    right_to_left.reverse()

    for i in range(len(nums)):
        if i == 0:
            answers.append(right_to_left[1])
        elif i == len(nums) - 1:
            answers.append(left_to_right[len(nums) - 2])
        else:
            answers.append(left_to_right[i - 1] * right_to_left[i + 1])

    return answers