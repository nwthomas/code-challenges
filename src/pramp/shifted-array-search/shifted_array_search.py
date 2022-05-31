"""
Shifted Array Search
A sorted array of distinct integers shiftArr is shifted to the left by an unknown offset and you don’t have a pre-shifted copy of it. For instance, the sequence 1, 2, 3, 4, 5 becomes 3, 4, 5, 1, 2, after shifting it twice to the left.

Given shiftArr and an integer num, implement a function shiftedArrSearch that finds and returns the index of num in shiftArr. If num isn’t in shiftArr, return -1. Assume that the offset can be any value between 0 and arr.length - 1.

Explain your solution and analyze its time and space complexities.

Example:
input:  shiftArr = [9, 12, 17, 2, 4, 5], num = 2 # shiftArr is the
                                                 # outcome of shifting
                                                 # [2, 4, 5, 9, 12, 17]
                                                 # three times to the left
output: 3 # since it’s the index of 2 in arr

Constraints:
[time limit] 5000ms
[input] array.integer arr
[input] integer num
[output] integer
"""

def shifted_arr_search(shift_arr, num):
    if len(shift_arr) <= 1:
        return -1 if len(shift_arr) < 1 or (len(shift_arr) == 1 and shift_arr[0] != num) else 0
    
    pivot = len(shift_arr) // 2
    left = 0
    right = len(shift_arr) - 1
    
    while left < right:
        if shift_arr[left] == num:
            return left
        elif shift_arr[right] == num:
            return right
        elif shift_arr[pivot] == num:
            return pivot
        
        if shift_arr[pivot] > shift_arr[right] and (shift_arr[pivot] < num or shift_arr[right] > num):
            left = pivot + 1
        elif shift_arr[pivot] > shift_arr[right]:
            right = pivot - 1
        elif shift_arr[pivot] > num or shift_arr[left] < num:
            right = pivot - 1
        else:
            left = pivot + 1
        
        pivot = len(shift_arr[left:right + 1]) // 2 + left
        
    return -1