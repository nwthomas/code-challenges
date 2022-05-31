"""
https://leetcode.com/problems/first-missing-positive/

Given an unsorted integer array nums, return the smallest missing positive integer.

You must implement an algorithm that runs in O(n) time and uses constant extra space.

Example 1:
Input: nums = [1,2,0]
Output: 3

Example 2:
Input: nums = [3,4,-1,1]
Output: 2

Example 3:
Input: nums = [7,8,9,11,12]
Output: 1

Constraints:
1 <= nums.length <= 5 * 105
-231 <= nums[i] <= 231 - 1
"""

from typing import List

def find_first_missing_positive(l: List[int]) -> int:
    for i in range(len(l)):
        correct_i = l[i] - 1
        
        while 0 < l[i] < len(l) + 1 and correct_i != i and l[i] != l[correct_i]:
            l[i], l[correct_i] = l[correct_i], l[i]
            correct_i = l[i] - 1
            
    for i, num in enumerate(l):
        if num != i + 1:
            return i + 1
        
    return len(l) + 1