"""
https://leetcode.com/problems/trapping-rain-water/

Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it can trap after raining.

Example 1:
Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6
Explanation: The above elevation map (black section) is represented by array [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section) are being trapped.

Example 2:
Input: height = [4,2,0,3,2,5]
Output: 9

Constraints:
n == height.length
1 <= n <= 2 * 104
0 <= height[i] <= 105
"""

from typing import List


def trap(heights: List[int]) -> int:
    """
    Compute how much water can be trapped after raining.

    Args:
        heights (List[int]): A list of non-negative integers representing an elevation map.

    Returns:
        int: The amount of water that can be trapped.
    """
    # Edge case: input is not a list
    if not isinstance(heights, list):
        raise TypeError("Arguments must be of type list")

    # Edge case: empty list
    if len(heights) < 1:
        return 0

    # Initialize variables to keep track of water trapped and maximum heights on both sides
    water_trapped = 0
    left = 0
    right = len(heights) - 1
    max_left = heights[left]
    max_right = heights[right]

    # Loop through the list until the two pointers meet
    while left < right:
        # Move the pointer that points to the smaller maximum height
        if max_left <= max_right:
            left += 1
        else:
            right -= 1

        # Update the trapped water and maximum heights for this iteration
        current_index = left if max_left <= max_right else right
        trapped = min(max_left, max_right) - heights[current_index]
        water_trapped += trapped if trapped > 0 else 0
        max_right = max(max_right, heights[right])
        max_left = max(max_left, heights[left])

    # Return the total amount of water that can be trapped
    return water_trapped
