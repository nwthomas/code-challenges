"""
https://leetcode.com/problems/maximum-subarray/description/

Given an integer array nums, find the subarray with the largest sum, and return its sum.

Example 1:
Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
Output: 6
Explanation: The subarray [4,-1,2,1] has the largest sum 6.

Example 2:
Input: nums = [1]
Output: 1
Explanation: The subarray [1] has the largest sum 1.

Example 3:
Input: nums = [5,4,-1,7,8]
Output: 23
Explanation: The subarray [5,4,-1,7,8] has the largest sum 23.
 
Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
 
Follow up: If you have figured out the O(n) solution, try coding another solution using the divide and conquer approach, which is more subtle.
"""

from typing import List

def max_sub_array(nums: List[int]) -> int:
    largest_sum = float('-inf')
    current_sum = 0
    has_reached_zero = False

    for num in nums:
        if current_sum + num < 0:
            current_sum = num
        else:
            current_sum += num
        
        if not has_reached_zero and current_sum >= 0:
            has_reached_zero = True
        
        if has_reached_zero:
            current_sum = max(0, current_sum)
        
        largest_sum = max(largest_sum, current_sum)
        
    return largest_sum