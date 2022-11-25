"""
You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation: 
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
"""

from heapq import heappop, heappush
from typing import List

def maxSlidingWindow(nums: List[int], k: int) -> List[int]:
    h = []
    tracker = {}
    
    right = 0
    
    while right < k:
        if not nums[right] in tracker: 
            tracker[nums[right]] = 0
            
        tracker[nums[right]] += 1
        heappush(h, nums[right] * -1)
        right += 1
        
    results = [h[0] * -1]
    left = 1
    
    tracker[nums[0]] -= 1
    
    while right < len(nums):
        if not nums[right] in tracker:
            tracker[nums[right]] = 0

        tracker[nums[right]] += 1
        heappush(h, nums[right] * -1)
        
        currentMax = h[0] * -1
        
        while tracker[currentMax] == 0:
            heappop(h)
            currentMax = h[0] * -1
            
        results.append(currentMax)
        
        tracker[nums[left]] -= 1
    
        left += 1
        right += 1
    
    return results