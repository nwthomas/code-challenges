"""
Write a function for doing an in-place shuffle of a list.

The shuffle must be "uniform," meaning each item in the original list must have the same probability of ending up in each spot in the final list.

Assume that you have a function get_random(floor, ceiling) for getting a random integer that is >= floor and <= ceiling.
"""
import random


def get_random(floor, ceiling):
    """Takes in floor and ceiling integers and returns a random number between them"""
    return random.randrange(floor, ceiling + 1)


def shuffle(num_list):
    """Takes in a list of values and shuffles them in place with the same probability of a value ending up in each spot"""
    if type(num_list) != list:
        raise TypeError("The argument for shuffle must be of type list.")
    elif len(num_list) <= 1:
        return num_list

    for i in range(0, len(num_list)):
        random_i = get_random(i, len(num_list) - 1)
        num_list[i], num_list[random_i] = num_list[random_i], num_list[i]
