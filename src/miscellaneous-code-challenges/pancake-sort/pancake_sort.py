"""
Given an array of integers arr:

1. Write a function flip(arr, k) that reverses the order of the first k elements in the array arr.
2. Write a function pancakeSort(arr) that sorts and returns the input array. You are allowed to use only the function flip you wrote in the first step in order to make changes in the array.

Example:
input:  arr = [1, 5, 4, 3, 2]

output: [1, 2, 3, 4, 5] # to clarify, this is pancakeSort's output
Analyze the time and space complexities of your solution.

Note: it's called pancake sort because it resembles sorting pancakes on a plate with a spatula, where you can only use the spatula to flip some of the top pancakes in the plate. To read more about the problem, see the Pancake Sorting Wikipedia page.

Constraints:
- [time limit] 5000ms
- [input] array.integer arr
- [input] integer k
- 0 ≤ k
- [output] array.integer
"""


def flip(arr: list[int], k: int):
    left = 0
    right = k - 1

    while left < right:
        arr[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

    return arr


def pancake_sort(arr: list[int]) -> list[int]:
    offset = 0

    while offset < len(arr):
        greatest_i = 0

        for i in range(len(arr) - offset):
            if arr[i] > arr[greatest_i]:
                greatest_i = i

        arr = flip(arr, greatest_i + 1)
        arr = flip(arr, len(arr) - offset)
        offset += 1

    return arr
