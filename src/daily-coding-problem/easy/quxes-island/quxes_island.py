"""
Good morning! Here's your coding interview problem for today.

This problem was asked by Facebook.

On a mysterious island there are creatures known as Quxes which come in three colors: red, green, and blue. One power of the Qux is that if two of them are standing next to each other, they can transform into a single creature of the third color.

Given N Quxes standing in a line, determine the smallest number of them remaining after any possible sequence of such transformations.

For example, given the input ['R', 'G', 'B', 'G', 'B'], it is possible to end up with a single Qux through the following steps:

        Arrangement       |   Change
----------------------------------------
['R', 'G', 'B', 'G', 'B'] | (R, G) -> B
['B', 'B', 'G', 'B']      | (B, G) -> R
['B', 'R', 'B']           | (R, B) -> G
['B', 'G']                | (B, G) -> R
['R']                     |
"""

from typing import List

def get_flipped_qux(q1: str, q2: str) -> str:
    if q1 == "R" and q2 == "B":
        return "G"
    elif q1 == "R" and q2 == "G":
        return "B"
    elif q1 == "B" and q2 == "R":
        return "G"
    elif q1 == "B" and q2 == "G":
        return "R"
    elif q1 == "G" and q2 == "R":
        return "B"
    else:
        return "R"

def get_smallest_quxes_number(quxes: List[str]) -> List[str]:
    has_flipped_during_iteration = False
    q = quxes
    i = 0

    while i < len(q):
        if i < len(q) - 1 and q[i] != q[i + 1]:
            flipped_qux = get_flipped_qux(q[i], q[i + 1])
            q = q[:i] + [flipped_qux] + q[i + 2:]
            has_flipped_during_iteration = True

        i += 1

        if i >= len(q) - 1 and has_flipped_during_iteration:
            has_flipped_during_iteration = False
            i = 0

    return q