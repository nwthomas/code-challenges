from subsets_ii import subsetsWithDup


def test_returns_all_possible_subsets_for_a_short_array_of_nums():
    result = subsetsWithDup([1, 2, 2])

    assert result == [
        [],
        [1],
        [1, 2],
        [1, 2, 2],
        [2],
        [2, 2],
    ]


def test_returns_all_possible_subsets_for_a_long_array_of_nums():
    result = subsetsWithDup([1, 2, 2, 3, 3, 3])

    assert result == [
        [],
        [1],
        [1, 2],
        [1, 2, 2],
        [1, 2, 2, 3],
        [1, 2, 2, 3, 3],
        [1, 2, 2, 3, 3, 3],
        [1, 2, 3],
        [1, 2, 3, 3],
        [1, 2, 3, 3, 3],
        [1, 3],
        [1, 3, 3],
        [1, 3, 3, 3],
        [2],
        [2, 2],
        [2, 2, 3],
        [2, 2, 3, 3],
        [2, 2, 3, 3, 3],
        [2, 3],
        [2, 3, 3],
        [2, 3, 3, 3],
        [3],
        [3, 3],
        [3, 3, 3],
    ]


def test_returns_all_possible_subsets_for_an_array_of_same_nums():
    result = subsetsWithDup([7, 7])

    assert result == [
        [],
        [7],
        [7, 7],
    ]
