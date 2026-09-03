/*
Given an array of integers heights representing the histogram's bar height where the width of each bar is 1, return the area of the largest rectangle in the histogram.

Example 1:
Input: heights = [2,1,5,6,2,3]
Output: 10
Explanation: The above is a histogram where width of each bar is 1.
The largest rectangle is shown in the red area, which has an area = 10 units.

Example 2:
Input: heights = [2,4]
Output: 4
 
Constraints:
1 <= heights.length <= 105
0 <= heights[i] <= 104
*/

function largestRectangleArea(heights) {
    let maxArea = 0;
    const stack = []; // [index, height]

    for (let i = 0; i < heights.length; i++) {
        const currentHeight = heights[i];
        let currentStart = i;

        while (stack.length > 0 && stack[stack.length - 1][1] > currentHeight) {
            const [topIndex, topHeight] = stack.pop();
            maxArea = Math.max(maxArea, topHeight * (i - topIndex));
            currentStart = topIndex;
        }

        stack.push([currentStart, currentHeight]);
    }

    for (const [i, h] of stack) {
        maxArea = Math.max(maxArea, h * (heights.length - i));
    }

    return maxArea;
}

module.exports = { largestRectangleArea };
