"""

Collect|
You have an array of numbers.
Your task is to sort ascending odd numbers but even numbers must be on their places.

Zero isn't an odd number and you don't need to move it. If you have an empty array, you need to return it.

Example

sort_array([5, 3, 2, 8, 1, 4]) == [1, 3, 2, 8, 5, 4]
"""
from copy import copy


def sort_array(num_list=[]):
    """Takes in a list of numbers and returns it with the odd sorted and the even not"""

    if type(num_list) != list:
        raise TypeError("The argument for sort_array must be of type list.")
    if len(num_list) < 1:
        return num_list

    odd_list = []
    odd_indices = []

    for i, num in enumerate(num_list):
        if num % 2 != 0:
            odd_list.append(num)
            odd_indices.append(i)

    sorted_odd_list = quick_sort(odd_list)
    final_list = copy(num_list)

    for i, num in enumerate(sorted_odd_list):
        final_index = odd_indices[i]
        final_list[final_index] = num

    return final_list


def quick_sort(num_list=[]):
    """Quick sorts a number list"""

    if type(num_list) != list:
        raise TypeError("The argument for quick_sort must be of type list.")
    if len(num_list) <= 1:
        return num_list

    choice = num_list[len(num_list) // 2]
    greater = [num for num in num_list if num > choice]
    equal = [num for num in num_list if num == choice]
    lesser = [num for num in num_list if num < choice]

    return quick_sort(lesser) + equal + quick_sort(greater)
