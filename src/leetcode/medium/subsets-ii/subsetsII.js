/*
https://leetcode.com/problems/subsets-ii/description

Given an integer array nums that may contain duplicates, return all possible subsets (the power set).

The solution set must not contain duplicate subsets. Return the solution in any order.

Example 1:
Input: nums = [1,2,2]
Output: [[],[1],[1,2],[1,2,2],[2],[2,2]]

Example 2:
Input: nums = [0]
Output: [[],[0]]
 
Constraints:
1 <= nums.length <= 10
-10 <= nums[i] <= 10
*/

const subsetsWithDup = (nums) => {
    nums.sort((a, b) => a - b);

    function backtrack(step = 0, subset = []) {
        if (step >= nums.length) {
            return [subset];
        }

        const result = [subset];
        let prev = -Infinity;
        for (let i = step; i < nums.length; i++) {
            const currentNum = nums[i];

            if (currentNum !== prev) {
                prev = currentNum;
                result.push(...backtrack(i + 1, [...subset, currentNum]));
            }
        }

        return result;
    }

    return backtrack();
};

module.exports = { subsetsWithDup };
