"""
Write an algorithm that takes an array and moves all of the zeros to the end, preserving the order of the other elements.

move_zeros([false,1,0,1,2,0,1,3,"a"]) # returns[false,1,1,2,1,3,"a",0,0]
"""


def move_zeros(array=None):
    if array is None or type(array) != list:
        return None
    other_values = []
    zeros = []
    for value in array:
        if value == 0 and type(value) != type(False):
            zeros.append(value)
        else:
            other_values.append(value)
    return other_values + zeros
