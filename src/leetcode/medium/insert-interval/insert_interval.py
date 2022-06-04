"""
https://leetcode.com/problems/insert-interval/

You are given an array of non-overlapping intervals intervals where intervals[i] = [starti, endi] represent the start and the end of the ith interval and intervals is sorted in ascending order by starti. You are also given an interval newInterval = [start, end] that represents the start and end of another interval.

Insert newInterval into intervals such that intervals is still sorted in ascending order by starti and intervals still does not have any overlapping intervals (merge overlapping intervals if necessary).

Return intervals after the insertion.

Example 1:
Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:
Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

Constraints:
0 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 105
intervals is sorted by starti in ascending order.
newInterval.length == 2
0 <= start <= end <= 105
"""

from typing import List

def insert(intervals: List[List[int]], new_interval: List[int]) -> List[List[int]]:
    if len(intervals) < 1:
        return [new_interval]
    
    output = []
    new_start, new_end = new_interval
    used_new_interval = False
    
    for interval in intervals:
        current_start, current_end = interval
        
        min_start = min(new_start, current_start)
        max_start = max(new_start, current_start)
        
        minEnd = min(new_end, current_end)
        maxEnd = max(new_end, current_end)
        
        if max_start <= minEnd and len(output) > 0 and output[len(output) - 1][1] > min_start:
            used_new_interval = min_start == new_start or max_start == new_start
            output[len(output) - 1][1] = maxEnd
        elif max_start <= minEnd:
            used_new_interval = min_start == new_start or max_start == new_start
            output.append([min_start, maxEnd])
        else:
            if not used_new_interval and new_interval[1] < current_start:
                output.append(new_interval)
                used_new_interval = True
            output.append(interval)
            
    if not used_new_interval:
        output.append(new_interval)
            
    return output