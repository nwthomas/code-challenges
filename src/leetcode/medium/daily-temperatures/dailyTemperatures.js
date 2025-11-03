/*
https://leetcode.com/problems/daily-temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
*/


const dailyTemperatures = (temperatures) => {
    const tracker = [];
    const result = Array(temperatures.length).fill(0)

    for (let i = 0; i < temperatures.length; i++) {
        if (tracker.length === 0) {
            tracker.push(i);
            continue;
        }

        const currentTemp = temperatures[i];
        while (tracker.length > 0 && currentTemp > temperatures[tracker[tracker.length-1]]) {
            const previousTempIndex = tracker.pop();
            result[previousTempIndex] = i - previousTempIndex;
        }

        tracker.push(i);
    }

    return result;
}

module.exports = { dailyTemperatures };