"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Stripe.

Write a function to flatten a nested dictionary. Namespace the keys with a period.

For example, given the following dictionary:

{
    "key": 3,
    "foo": {
        "a": 5,
        "bar": {
            "baz": 8
        }
    }
}
it should become:

{
    "key": 3,
    "foo.a": 5,
    "foo.bar.baz": 8
}
You can assume keys do not contain dots in them, i.e. no clobbering will occur.
"""
from copy import deepcopy


def flatten_nested_dictionary(base="", dictionary={}):
    """
    Takes in a dictionary and flattens it
    """
    flattened_dict = {}
    if type(dictionary) != dict:
        raise TypeError(
            "The argument passed into flatten_nested_dictionary must be of type 'dict'")
    if len(dictionary.keys()) <= 0:
        return flattened_dict
    stack = [(base + "." + key, dictionary[key]) if len(base) >
             0 else (key, dictionary[key]) for key in dictionary]
    while len(stack) >= 1:
        tup = stack.pop()
        if type(tup[1]) == dict:
            flattened_dict.update(flatten_nested_dictionary(tup[0], tup[1]))
        else:
            flattened_dict[tup[0]] = tup[1]
    return flattened_dict
