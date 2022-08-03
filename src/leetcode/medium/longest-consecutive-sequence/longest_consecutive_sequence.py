"""
https://leetcode.com/problems/longest-consecutive-sequence

Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

You must write an algorithm that runs in O(n) time.

Example 1:
Input: nums = [100,4,200,1,3,2]
Output: 4
Explanation: The longest consecutive elements sequence is [1, 2, 3, 4]. Therefore its length is 4.

Example 2:
Input: nums = [0,3,7,2,5,8,4,6,0,1]
Output: 9

Constraints:
0 <= nums.length <= 105
-109 <= nums[i] <= 109
"""

from heapq import heappop, heappush
from typing import List

def longest_consecutive_with_heap(nums: List[int]) -> int:
    if len(nums) < 1:
        return 0
    
    heap = []
    longest_consecutive = 0
    current_consecutive = 0
    prev_num = None
    
    for num in nums:
        heappush(heap, num)
    
    prev_num = heappop(heap)
    longest_consecutive = 1
    current_consecutive = 1
    
    while len(heap) > 0:
        current_num = heappop(heap)

        if current_num == prev_num:
            continue
        elif current_num == prev_num + 1:
            current_consecutive += 1
            longest_consecutive = max(longest_consecutive, current_consecutive)
        else:
            current_consecutive = 1
        
        prev_num = current_num
        
    return longest_consecutive

def longest_consecutive_with_set(nums: List[int]) -> int:
    if len(nums) < 1:
        return 0

    nums_set = set(nums)
    longest_sequence = 1

    for num in nums_set:
        if num - 1 not in nums_set:
            current_num = num
            current_sequence = 1

            while current_num + 1 in nums_set:
                current_num += 1
                current_sequence += 1
                longest_sequence = max(longest_sequence, current_sequence)

    return longest_sequence