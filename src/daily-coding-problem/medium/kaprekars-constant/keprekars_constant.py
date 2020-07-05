"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Salesforce.

The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:

For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
Subtract the smaller number from the larger number.
For example, this algorithm terminates in three steps when starting from 1234:

4321 - 1234 = 3087
8730 - 0378 = 8352
8532 - 2358 = 6174
Write a function that returns how many steps this will take for a given input N.
"""
from random import randint


def find_keprekars_constant_steps(number, steps=0):
    """
    Takes in a number and finds the Keprekar's Constant in N number of steps.

    Arguments:
        number - int
    """
    if (number == 6174):
        return steps

    number_1_list = quick_sort([char for char in str(number)])
    number_1_reversed = number_1_list[::-1]
    number_1 = int("".join(number_1_list))
    number_2 = int("".join(number_1_reversed))

    result = number_1 - number_2 if number_1 >= number_2 else number_2 - number_1

    return find_keprekars_constant_steps(result, steps + 1)


def quick_sort(l):
    if len(l) <= 1:
        return l
    else:
        pivot = l[randint(0, len(l) - 1)]
        less = [i for i in l if i < pivot]
        equal = [i for i in l if i == pivot]
        greater = [i for i in l if i > pivot]
        return quick_sort(greater) + equal + quick_sort(less)
