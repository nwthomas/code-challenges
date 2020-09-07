"""
In order to win the prize for most cookies sold, my friend Alice and I are going to merge our Girl Scout Cookies orders and enter as one unit.

Each order is represented by an "order id" (an integer).

We have our lists of orders sorted numerically already, in lists. Write a function to merge our lists of orders into one sorted list.

For example:

my_list     = [3, 4, 6, 10, 11, 15]
alices_list = [1, 5, 8, 12, 14, 19]

# Prints [1, 3, 4, 5, 6, 8, 10, 11, 12, 14, 15, 19]
print(merge_lists(my_list, alices_list))
"""


def merge_sorted_cookie_lists(listA, listB):
    """Takes in two order lists of cookies and merges them together"""
    if type(listA) != list or type(listB) != list:
        raise TypeError(
            "Both arguments for merge_sorted_cookie_lists must be of type list.")

    final_list = []
    listA_length = len(listA)
    listB_length = len(listB)

    if listA_length < 1:
        return listB
    if listB_length < 1:
        return listA
    if listB_length < 1 and listA_length < 1:
        return final_list

    a_index = 0
    b_index = 0

    while a_index + b_index < listA_length + listB_length:
        if a_index >= listA_length:
            final_list.append(listB[b_index])
            b_index += 1
        elif b_index >= listB_length:
            final_list.append(listA[a_index])
            a_index += 1
        elif listB[b_index] < listA[a_index]:
            final_list.append(listB[b_index])
            b_index += 1
        else:
            final_list.append(listA[a_index])
            a_index += 1

    return final_list
