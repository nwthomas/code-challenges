/*
https://leetcode.com/problems/meeting-rooms-ii

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), find the minimum number of days required to schedule all meetings without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8.

Example 1:
Input: intervals = [(0,40),(5,10),(15,20)]
Output: 2
Explanation:
day1: (0,40)
day2: (5,10),(15,20)

Example 2:
Input: intervals = [(4,9)]
Output: 1

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
*/

import { heapPop, heapPush } from "heapq";

class Interval {
    start: number;
    end: number;

    constructor(start: number, end: number) {
        this.start = start;
        this.end = end;
    }
}

const getMinimumMeetingRoomsCount = (intervals: Interval[]) => {
    intervals = intervals.sort((a, b) => a.start - b.start);
    const minHeap: number[] = [];

    for (const interval of intervals) {
        if (minHeap.length > 0 && minHeap[0] <= interval.start) {
            heapPop(minHeap);
        }
        heapPush(minHeap, interval.end);
    }

    return minHeap.length;
};

export { getMinimumMeetingRoomsCount, Interval };
