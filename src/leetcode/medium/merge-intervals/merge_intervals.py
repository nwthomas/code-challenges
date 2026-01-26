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


def merge(intervals: list[list[int]]) -> list[list[int]]:
    output = []

    def get_sort_val(interval):
        return interval[0]

    intervals.sort(key=get_sort_val)

    for interval in intervals:
        current_start, current_end = interval

        if len(output) < 1:
            output.append(interval)
        else:
            prev_start, prev_end = output[len(output) - 1]

            max_start = max(prev_start, current_start)

            min_end = min(prev_end, current_end)
            max_end = max(prev_end, current_end)

            if max_start <= min_end:
                output[len(output) - 1][1] = max_end
            else:
                output.append(interval)

    return output
