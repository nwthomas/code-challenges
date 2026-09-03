import pytest
from pairs_with_specific_difference import find_pairs_with_given_difference


@pytest.mark.parametrize("arr, k, expected", [
    # Basic case
    (
        [0, -1, -2, 2, 1],
        1,
        [[1, 0], [0, -1], [-1, -2], [2, 1]]
    ),

    # Multiple pairs
    (
        [1, 5, 11, 7],
        4,
        [[5, 1], [11, 7]]
    ),

    # No pairs
    (
        [1, 2, 3, 4],
        10,
        []
    ),

    # Output order must follow y's position in arr
    (
        [4, 1, 3, 2],
        1,
        [[2, 1], [4, 3], [3, 2]]
    ),

    # Negative numbers
    (
        [-5, -2, -8, 1],
        3,
        [[-2, -5], [1, -2], [-5, -8]]
    ),

    # Single element
    (
        [10],
        5,
        []
    ),

    # Empty array
    (
        [],
        3,
        []
    ),

    # k = 0: elements are distinct, so no x != y pair exists
    (
        [3, 1, 7, 5],
        0,
        []
    ),

    # Larger difference
    (
        [100, 0, 50, -50],
        50,
        [[50, 0], [100, 50], [0, -50]]
    ),

    # Two elements that form a pair
    (
        [1, 2],
        1,
        [[2, 1]]
    ),

    # Two elements in reverse order
    (
        [2, 1],
        1,
        [[2, 1]]
    ),

    # Two elements with no pair
    (
        [1, 3],
        1,
        []
    ),

    # Negative and positive values
    (
        [-3, 0, 3, 6],
        3,
        [[0, -3], [3, 0], [6, 3]]
    ),

    # Input order very different from numeric order
    (
        [10, 4, 7, 1],
        3,
        [[7, 4], [10, 7], [4, 1]]
    ),

    # Large k
    (
        [-100, 100, 0],
        200,
        [[100, -100]]
    ),

    # Negative y with positive x
    (
        [5, -5, 0],
        5,
        [[0, -5], [5, 0]]
    ),
])
def test_find_pairs_with_given_difference(arr, k, expected):
    assert find_pairs_with_given_difference(arr, k) == expected
