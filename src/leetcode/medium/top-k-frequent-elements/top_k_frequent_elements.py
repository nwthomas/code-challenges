"""
https://leetcode.com/problems/top-k-frequent-elements/

Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

Example 1:
Input: nums = [1,1,1,2,2,3], k = 2
Output: [1,2]

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
k is in the range [1, the number of unique elements in the array].
It is guaranteed that the answer is unique.

Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.
"""

from typing import List

def top_k_frequent(nums: List[int], k: int) -> List[int]:
    count_to_nums = [set(), set()]
    num_to_count = {}
    
    for num in nums:
        if not num in num_to_count:
            num_to_count[num] = 0
        elif num_to_count[num] > 0:
            count_to_nums[num_to_count[num]].remove(num)
        
        num_to_count[num] += 1
        
        if len(count_to_nums) - 1 < num_to_count[num]:
            count_to_nums.append(set())
            
        count_to_nums[num_to_count[num]].add(num)
        
    results = []
    current = None
    
    while len(results) < k and len(count_to_nums) > 0:
        current = count_to_nums.pop()
        
        for value in current:
            if len(results) < k:
                results.append(value)
            else:
                break
    
    return results