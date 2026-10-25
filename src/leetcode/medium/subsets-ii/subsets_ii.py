"""
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
"""


def subsetsWithDup(nums: list[int]) -> list[list[int]]:
    nums.sort()

    def backtrack(step: int, subset: list[int]) -> list[list[int]]:
        if step > len(nums) - 1:
            return [subset]

        results = [subset]
        prev = -float('inf')

        for i in range(step, len(nums)):
            currentNum = nums[i]

            if currentNum != prev:
                prev = currentNum
                results.extend(backtrack(i + 1, [*subset, currentNum]))

        return results

    return backtrack(0, [])
