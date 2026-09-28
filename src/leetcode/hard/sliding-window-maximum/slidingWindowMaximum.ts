/*
https://leetcode.com/problems/sliding-window-maximum

You are given an array of integers nums, there is a sliding window of size k which is moving from the very left of the array to the very right. You can only see the k numbers in the window. Each time the sliding window moves right by one position.

Return the max sliding window.

Example 1:
Input: nums = [1,3,-1,-3,5,3,6,7], k = 3
Output: [3,3,5,5,6,7]
Explanation:
Window position                Max
---------------               -----
[1  3  -1] -3  5  3  6  7       3
 1 [3  -1  -3] 5  3  6  7       3
 1  3 [-1  -3  5] 3  6  7       5
 1  3  -1 [-3  5  3] 6  7       5
 1  3  -1  -3 [5  3  6] 7       6
 1  3  -1  -3  5 [3  6  7]      7

Example 2:
Input: nums = [1], k = 1
Output: [1]

Constraints:
1 <= nums.length <= 105
-104 <= nums[i] <= 104
1 <= k <= nums.length
*/

import { heapPush, heapPop } from "heapq";

function comparator(a: number[], b: number[]) {
    return a[0] < b[0];
}

function slidingWindowMaximum(nums: number[], k: number) {
    const heap: number[][] = [];
    const result = [];
    let i = 0;

    while (i < k) {
        heapPush(heap, [nums[i] * -1, i], { comparator });
        i += 1;
    }

    result.push(heap[0][0] * -1);

    while (i < nums.length) {
        heapPush(heap, [nums[i] * -1, i], { comparator });

        while (heap[0][1] <= i - k) {
            heapPop(heap, { comparator });
        }

        result.push(heap[0][0] * -1);
        i += 1;
    }

    return result;
}

export { slidingWindowMaximum };
