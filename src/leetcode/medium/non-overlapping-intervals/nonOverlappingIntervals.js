/*
https://leetcode.com/problems/non-overlapping-intervals/

Given an array of intervals intervals where intervals[i] = [starti, endi], return the minimum number of intervals you need to remove to make the rest of the intervals non-overlapping.

Example 1:
Input: intervals = [[1,2],[2,3],[3,4],[1,3]]
Output: 1
Explanation: [1,3] can be removed and the rest of the intervals are non-overlapping.

Example 2:
Input: intervals = [[1,2],[1,2],[1,2]]
Output: 2
Explanation: You need to remove two [1,2] to make the rest of the intervals non-overlapping.

Example 3:
Input: intervals = [[1,2],[2,3]]
Output: 0
Explanation: You don't need to remove any of the intervals since they're already non-overlapping.

Constraints:
1 <= intervals.length <= 105
intervals[i].length == 2
-5 * 104 <= starti < endi <= 5 * 104
*/

const eraseOverlapIntervals = (intervals) => {
    intervals = intervals.sort((a, b) => a[0] - b[0]);
    let prevEnd = intervals[0][1];
    let removed = 0;

    for (let i = 1; i < intervals.length; i++) {
        const start = intervals[i][0]
        const end = intervals[i][1];

        if (prevEnd <= start) {
            prevEnd = end;
        } else {
            removed++;
            prevEnd = Math.min(end, prevEnd);
        }
    }

    return removed;
}

module.exports = { eraseOverlapIntervals };