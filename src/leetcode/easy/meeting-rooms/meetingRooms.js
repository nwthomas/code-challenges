/*
https://leetcode.com/problems/meeting-rooms/

Given an array of meeting time interval objects consisting of start and end times [[start_1,end_1],[start_2,end_2],...] (start_i < end_i), determine if a person could add all meetings to their schedule without any conflicts.

Note: (0,8),(8,10) is not considered a conflict at 8

Example 1:
Input: intervals = [(0,30),(5,10),(15,20)]
Output: false
Explanation:
(0,30) and (5,10) will conflict
(0,30) and (15,20) will conflict

Example 2:
Input: intervals = [(5,8),(9,15)]
Output: true

Constraints:
0 <= intervals.length <= 500
0 <= intervals[i].start < intervals[i].end <= 1,000,000
*/

class Interval {
    constructor(start, end) {
        this.start = start;
        this.end = end;
    }
}

const scanAttendMeetings = (intervals) => {
    if (intervals.length <= 1) {
        return true;
    }

    const sortedIntervals = intervals.sort((a, b) => a.start - b.start);

    let latestEndSeen = sortedIntervals[0].end;
    for (let i = 1; i < sortedIntervals.length; i++) {
        const currentStart = sortedIntervals[i].start;
        if (currentStart < latestEndSeen) {
            return false;
        }

        latestEndSeen = sortedIntervals[i].end;
    }

    return true;
}

module.exports = { scanAttendMeetings, Interval };