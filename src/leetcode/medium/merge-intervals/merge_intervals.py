"""
https://leetcode.com/problems/merge-intervals

Given an array of intervals where intervals[i] = [starti, endi], merge all overlapping intervals, and return an array of the non-overlapping intervals that cover all the intervals in the input.

Example 1:
Input: intervals = [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:
Input: intervals = [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considered overlapping.

Constraints:
1 <= intervals.length <= 104
intervals[i].length == 2
0 <= starti <= endi <= 104
"""

from typing import List

def merge(intervals: List[List[int]]) -> List[List[int]]:
    output = []
    
    def getStartVal(interval):
        return interval[0]
    
    intervals.sort(key=getStartVal)
    
    for interval in intervals:
        currentStart, currentEnd = interval
        
        if len(output) < 1:
            output.append(interval)
        else:
            prevStart, prevEnd = output[len(output) - 1]
            
            maxStart = max(prevStart, currentStart)
            
            minEnd = min(prevEnd, currentEnd)
            maxEnd = max(prevEnd, currentEnd)
            
            if maxStart <= minEnd:
                output[len(output) - 1][1] = maxEnd
            else:
                output.append(interval)
                
    return output