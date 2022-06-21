"""
https://leetcode.com/problems/daily-temperatures

Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.

Example 1:
Input: temperatures = [73,74,75,71,69,72,76,73]
Output: [1,1,4,2,1,1,0,0]

Example 2:
Input: temperatures = [30,40,50,60]
Output: [1,1,1,0]

Example 3:
Input: temperatures = [30,60,90]
Output: [1,1,0]

Constraints:
1 <= temperatures.length <= 105
30 <= temperatures[i] <= 100
"""

from typing import List

def daily_temperatures(temperatures: List[int]) -> List[int]:
    stack = [[temperatures[0], 0]]
    results = [0 for _ in range(len(temperatures))]
    
    for current_index, temp in enumerate(temperatures):
        while len(stack) > 0 and temp > stack[len(stack) - 1][0]:
            value, value_index = stack.pop()
            number_of_days = current_index - value_index
            results[value_index] = number_of_days
            
        stack.append([temp, current_index])
        
    return results