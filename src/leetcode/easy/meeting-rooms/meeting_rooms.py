"""
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time intervals consisting of start and end times[[s1,e1],[s2,e2],...](si< ei), determine if a person could attend all meetings.

Example 1:
Input:
[[0,30],[5,10],[15,20]]
Output:
false

Example 2:
Input:
[[7,10],[2,4]]
Output:
true
"""

from typing import List

def can_person_attend_all_meetings(intervals: List[List[int]]) -> bool:
    if len(intervals) <= 1:
        return True

    def get_sorting_key(interval: List[int]):
        return interval[0]

    intervals.sort(key=get_sorting_key)

    prev_end = intervals[0][1]

    for i in range(1, len(intervals)):
        current_start, current_end = intervals[i]

        if current_start <= prev_end:
            return False
        else:
            prev_end = current_end

    return True