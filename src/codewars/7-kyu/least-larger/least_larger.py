"""
Task
Given an array of numbers and an index, return the index of the least number larger than the element at the given index, or -1 if there is no such index ( or, where applicable, Nothing or a similarly empty value ).

Notes
Multiple correct answers may be possible. In this case, return any one of them.
The given index will be inside the given array.
The given array will, therefore, never be empty.

Example
least_larger( [4, 1, 3, 5, 6], 0 )  ->  3
least_larger( [4, 1, 3, 5, 6], 4 )  -> -1
"""

def least_larger(num_list, index): 
    element = num_list[index]
    least_larger = None
    
    for i, num in enumerate(num_list):
        if num > element:
            if not least_larger:
                least_larger = (num, i)
            elif num < least_larger[0]:
                least_larger = (num, i)
    
    return least_larger[1] if least_larger else -1