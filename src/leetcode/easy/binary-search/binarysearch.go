/*
https://leetcode.com/problems/binary-search/

You are given an array of distinct integers nums, sorted in ascending order, and an integer target.

Implement a function to search for target within nums. If it exists, then return its index, otherwise, return -1.

Your solution must run in O(log n) time.

Example 1:
Input: nums = [-1,0,2,4,6,8], target = 4
Output: 3

Example 2:
Input: nums = [-1,0,2,4,6,8], target = 3
Output: -1

Constraints:
1 <= nums.length <= 10000.
-10000 < nums[i], target < 10000
All the integers in nums are unique.
*/

package binarysearch

func binarySearch(nums []int, target int) int {
    left := 0
    right := len(nums) - 1

    for left <= right {
        choice := ((right - left) / 2) + left

        leftNum := nums[left]
        rightNum := nums[right]
        choiceNum := nums[choice]
        
        if leftNum == target {
            return left
        } else if rightNum == target {
            return right
        } else if choiceNum == target {
            return choice
        }

        if left == right {
            return -1
        } else if choiceNum > target {
            right = choice
        } else if choice != left {
            left = choice
        } else {
            left += 1
        }
    }

    return -1
}
