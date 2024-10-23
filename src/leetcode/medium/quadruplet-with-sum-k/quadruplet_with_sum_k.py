"""
Given an array arr[] and a target value, the task is to find the count of quadruplets present in the given array having sum equal to the given target. 

Examples:

Input: arr[] = {1, 5, 3, 1, 2, 10}, target = 20
Output: 1
Explanation: Only quadruplet satisfying the conditions is arr[1] + arr[2] + arr[4] + arr[5] = 5 + 3 + 2 + 10 = 20.

Input: arr[] = {4, 5, 3, 1, 2, 4}, target = 13
Output: 3
Explanation: Three quadruplets with sum 13 are: 
arr[0] + arr[2] + arr[4] + arr[5] = 4 + 3 + 2 + 4 = 13
arr[0] + arr[1] + arr[2] + arr[3] = 4 + 5 + 3 + 1 = 13
arr[1] + arr[2] + arr[3] + arr[5] = 5 + 3 + 1 + 4 = 13

Input: arr[] = {1, 1, 1, 1, 1}, target = 4
Output: 5
Explanation: 
arr[0] + arr[1] + arr[2] + arr[3]  = 4
arr[0] + arr[1] + arr[3] + arr[4] = 4
arr[0] + arr[1] + arr[2] + arr[4] = 4
arr[0] + arr[2] + arr[3] + arr[4] = 4
arr[1] + arr[2] + arr[3] + arr[4] = 4
"""

from collections import defaultdict

def count_sum(arr, target):
    count = 0
    n = len(arr)
    m = defaultdict(int)

    for i in range(n - 1):
        for j in range(i + 1, n):
            temp = arr[i] + arr[j]
            if temp < target:
                count += m[target - temp]

        for j in range(i):
            temp = arr[i] + arr[j]
            if temp < target:
                m[temp] += 1

    return count