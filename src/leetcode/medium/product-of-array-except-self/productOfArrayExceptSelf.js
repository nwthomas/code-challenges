/*
https://leetcode.com/problems/product-of-array-except-self/

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.

Example 1:
Input: nums = [1,2,3,4]
Output: [24,12,8,6]

Example 2:
Input: nums = [-1,1,0,-3,3]
Output: [0,0,9,0,0]

Constraints:
2 <= nums.length <= 105
-30 <= nums[i] <= 30
The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

Follow up: Can you solve the problem in O(1) extra space complexity? (The output array does not count as extra space for space complexity analysis.)
*/

/**
 * @param {number[]} nums
 * @return {number[]}
 */
function getMultipliedNums(nums) {
    const multipliedNums = [];

    nums.forEach((num, i) => {
        if (!i) {
            multipliedNums.push(num);
        } else {
            multipliedNums.push(num * multipliedNums[i - 1]);
        }
    });

    return multipliedNums;
}

function productExceptSelf(nums) {
    if (nums.length <= 2) {
        return nums.reverse();
    }

    const multiplyRight = getMultipliedNums(nums);
    const multiplyLeft = getMultipliedNums(nums.reverse()).reverse();
    const answer = [];

    for (let i = 0; i < nums.length; i++) {
        if (i === 0) {
            answer.push(multiplyLeft[1]);
        } else if (i === nums.length - 1) {
            answer.push(multiplyRight[i - 1]);
        } else {
            answer.push(multiplyRight[i - 1] * multiplyLeft[i + 1]);
        }
    }

    return answer;
}

module.exports = {
    getMultipliedNums,
    productExceptSelf,
};
