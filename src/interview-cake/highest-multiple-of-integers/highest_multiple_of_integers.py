"""
Given a list of integers, find the highest product you can get from three of the integers.

The input list_of_ints will always have at least three integers.
"""


def find_highest_multiple_of_three_ints(int_list):
    """Takes in a list of integers and finds the highest multiple of three of them"""
    if type(int_list) != list:
        raise TypeError(
            "The argument for find_highest_multiple_of_three_ints must be of type list.")
    elif len(int_list) == 3:
        one, two, three = int_list
        return one * two * three

    highest_product_of_3 = int_list[0] * int_list[1] * int_list[2]
    highest_product_of_2 = int_list[0] * int_list[1]
    lowest_product_of_2 = int_list[0] * int_list[1]
    highest = max(int_list[0], int_list[1])
    lowest = min(int_list[0], int_list[1])

    for i in range(2, len(int_list)):
        current = int_list[i]

        highest_product_of_3 = max(
            highest_product_of_3, highest_product_of_2 * current, lowest_product_of_2 * current)

        highest_product_of_2 = max(
            highest_product_of_2, current * lowest, current * highest)

        lowest_product_of_2 = min(
            lowest_product_of_2, current * highest, current * lowest)

        highest = max(highest, current)

        lowest = min(lowest, current)

    return highest_product_of_3
