"""
You are given an array and you need to find number of tripets of indices (i, j, k) such that the elements at those indices are in geometric progression for a given common ratio r and i < j < k.

Example
arr  = [1, 4, 16, 64]
r = 4

There are [1, 4, 16] and [4, 16, 64] at indices [0, 1, 2] and [1, 2, 3]. Return 2.

Function Description

Complete the countTriplets function in the editor below.

countTriplets has the following parameter(s):

- int arr[n]: an array of integers
- int r: the common ratio

Returns

- int: the number of triplets
"""

def countTriplets(arr, r):
    rightOfIndex = {}
    leftOfIndex = {}
    tripletCount = 0

    for val in arr:
        rightOfIndex[val] = rightOfIndex[val] + 1 if val in rightOfIndex else 1

    for val in arr:
        firstValue = val / r
        thirdValue = val * r
        
        rightOfIndex[val] -= 1
        
        if firstValue in leftOfIndex and thirdValue in rightOfIndex and val % r == 0:
            tripletCount += leftOfIndex[firstValue] * rightOfIndex[thirdValue]
            
        leftOfIndex[val] = leftOfIndex[val] + 1 if val in leftOfIndex else 1
            
    return tripletCount