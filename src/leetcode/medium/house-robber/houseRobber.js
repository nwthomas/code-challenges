/*
https://leetcode.com/problems/house-robber/description/

You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.

Example 1:
Input: nums = [1,2,3,1]
Output: 4
Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
Total amount you can rob = 1 + 3 = 4.

Example 2:
Input: nums = [2,7,9,3,1]
Output: 12
Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
Total amount you can rob = 2 + 9 + 1 = 12.
 
Constraints:
1 <= nums.length <= 100
0 <= nums[i] <= 400
*/

const rob = (nums) => {
    const tracker = Array(nums.length).fill(0);
    let max = 0;

    for (let i = 0; i < nums.length; i++) {
        if (i < 2) {
            tracker[i] = nums[i];
        }
        if (i - 2 >= 0) {
            tracker[i] = tracker[i - 2] + nums[i];
        }
        if (i - 3 >= 0) {
            tracker[i] = Math.max(tracker[i], tracker[i - 3] + nums[i]);
        }

        max = Math.max(max, tracker[i])
    }

    return max;
}

module.exports = { rob };