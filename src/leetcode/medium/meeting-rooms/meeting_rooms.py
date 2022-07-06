"""
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times [s1, e1], [s2, e2], ... , determine if a person could attend all meetings.

For example,
Given [ [0, 30], [5, 10], [15, 20] ],
return false.
"""

from typing import List

def get_minimum_meeting_rooms_count(intervals: List[List[int]]) -> int:
    def get_sort_value(interval: List[int]) -> int:
        return interval[0]

    intervals.sort(key=get_sort_value)

    if len(intervals) < 1:
        return 0

    rooms_needed = 0
    prev_ends = [intervals[0][1]]

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]

        while len(prev_ends) > 0 and prev_ends[len(prev_ends) - 1] < current_start:
            prev_ends.pop()
            
        prev_ends.append(current_end)

        rooms_needed = max(rooms_needed, len(prev_ends))

    return rooms_needed