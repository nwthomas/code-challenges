from pancake_sort import pancake_sort


def test_sorts_input_arr():
    arr = [1, 5, 4, 3, 2]
    assert pancake_sort(arr) == [1, 2, 3, 4, 5]


def test_handles_list_length_one():
    arr = [1]
    assert pancake_sort(arr) == [1]


def test_handles_in_order():
    arr = [1, 2]
    assert pancake_sort(arr) == [1, 2]


def test_handles_duplicate_elements():
    arr = [1, 3, 1]
    assert pancake_sort(arr) == [1, 1, 3]


def test_handles_longer_lists():
    arr = [3, 1, 2, 4, 6, 5, 10, 9, 8]
    assert pancake_sort(arr) == [1, 2, 3, 4, 5, 6, 8, 9, 10]


def test_handles_huge_lists():
    arr = [10, 9, 8, 6, 7, 5, 4, 3, 2, 1, 9, 10, 8, 7,
           6, 5, 4, 3, 2, 1, 10, 9, 8, 7, 6, 5, 4, 3, 2, 1]
    assert pancake_sort(arr) == [1, 1, 1, 2, 2, 2, 3, 3, 3, 4, 4,
                                 4, 5, 5, 5, 6, 6, 6, 7, 7, 7, 8, 8, 8, 9, 9, 9, 10, 10, 10]
