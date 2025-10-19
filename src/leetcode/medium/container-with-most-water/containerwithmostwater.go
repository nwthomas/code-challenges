/*
https://leetcode.com/problems/container-with-most-water/

You are given an integer array height of length n. There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

Find two lines that together with the x-axis form a container, such that the container contains the most water.

Return the maximum amount of water a container can store.

Notice that you may not slant the container.

Example 1:
Input: height = [1,8,6,2,5,4,8,3,7]
Output: 49
Explanation: The above vertical lines are represented by array [1,8,6,2,5,4,8,3,7]. In this case, the max area of water (blue section) the container can contain is 49.

Example 2:
Input: height = [1,1]
Output: 1

Constraints:
n == height.length
2 <= n <= 105
0 <= height[i] <= 104
*/

package containerwithmostwater

func containerWithMostWater(heights []int) int {
    left := 0
    right := len(heights) - 1
    mostWater := 0

    for left < right {
        leftHeight := heights[left]
        rightHeight := heights[right]

        height := leftHeight
        if height > rightHeight {
            height = rightHeight
        }

        length := right - left
        currentWater := length * height

        if currentWater > mostWater {
            mostWater = currentWater
        }

        if leftHeight > rightHeight {
            right -= 1
        } else {
            left += 1
        }
    }

    return mostWater
}
