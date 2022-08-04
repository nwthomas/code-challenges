"""
https://leetcode.com/problems/median-of-two-sorted-arrays

Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.

The overall run time complexity should be O(log (m+n)).

Example 1:
Input: nums1 = [1,3], nums2 = [2]
Output: 2.00000
Explanation: merged array = [1,2,3] and median is 2.

Example 2:
Input: nums1 = [1,2], nums2 = [3,4]
Output: 2.50000
Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

Constraints:
nums1.length == m
nums2.length == n
0 <= m <= 1000
0 <= n <= 1000
1 <= m + n <= 2000
-106 <= nums1[i], nums2[i] <= 106
"""

from typing import List

def find_median_sorted_arrays(nums1: List[int], nums2: List[int]) -> float:
    A, B = nums1, nums2
    total = len(A) + len(B)
    half = total // 2

    if len(B) < len(A):
        A, B = B, A

    left = 0
    right = len(A) - 1

    while True:
        i = (left + right) // 2
        j = half - i - 2

        left_a = A[i] if i >= 0 else float("-inf")
        right_a = A[i + 1] if (i + 1) < len(A) else float('inf')
        left_b = B[j] if j >= 0 else float('-inf')
        right_b = B[j + 1] if (j + 1) < len(B) else float('inf')

        if left_a <= right_b and left_b <= right_a and total % 2:
            return min(right_a, right_b)
        elif left_a <= right_b and left_b <= right_a:
            return (max(left_a, left_b) + min(right_a, right_b)) / 2
        elif left_a > right_b:
            right = i - 1
        else:
            left = i + 1


