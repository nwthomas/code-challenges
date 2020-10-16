"""
Write a function get_products_of_all_ints_except_at_index() that takes a list of integers and returns a list of the products.

For example, given:
[1, 7, 3, 4]

your function would return:
[84, 12, 28, 21]

by calculating:
[7 * 3 * 4,  1 * 3 * 4,  1 * 7 * 4,  1 * 7 * 3]

Python 3.6
Here's the catch: You can't use division in your solution!
"""
from copy import copy


def get_products_of_all_ints_except_at_index(int_list):
    """Takes in a list of ints and returns the product for each except"""

    if type(int_list) != list:
        raise TypeError(
            "The argument for get_products_of_all_ints_except_at_index must be of type list.")
    if len(int_list) <= 1:
        raise Exception("The length of the integer list must be 2 or greater.")

    product_list = [None] * len(int_list)
    product_so_far = 1

    for i in range(0, len(int_list)):
        product_list[i] = product_so_far
        product_so_far *= int_list[i]

    product_so_far = 1

    for i in range(len(int_list) - 1, -1, -1):
        product_list[i] *= product_so_far
        product_so_far *= int_list[i]

    return product_list
