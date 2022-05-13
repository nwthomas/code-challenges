"""
https://leetcode.com/problems/maximum-product-subarray/submissions/

Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.

The test cases are generated so that the answer will fit in a 32-bit integer.

A subarray is a contiguous subsequence of the array.

Example 1:

Input: nums = [2,3,-2,4]
Output: 6
Explanation: [2,3] has the largest product 6.
Example 2:

Input: nums = [-2,0,-1]
Output: 0
Explanation: The result cannot be 2, because [-2,-1] is not a subarray.

Constraints:

1 <= nums.length <= 2 * 104
-10 <= nums[i] <= 10
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.
"""

from typing import List

def max_product(nums: List[int]) -> int:
    if len(nums) == 1:
        return nums[0]
    
    max_so_far = max(nums)
    max_current = 1
    min_current = 1
    
    for _, num in enumerate(nums):            
        if num == 0:
            max_current = 1
            min_current = 1
            continue

        temp_max_current = max_current * num
        max_current = max(temp_max_current, num * min_current, num)
        min_current = min(temp_max_current, num * min_current, num)
        max_so_far = max(max_so_far, max_current)
            
    return max_so_far