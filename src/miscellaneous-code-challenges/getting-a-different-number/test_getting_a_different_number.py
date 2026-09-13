from getting_a_different_number import get_different_number


def test_returns_zero_if_missing():
    result = get_different_number([1, 2, 3, 4])
    assert result == 0


def test_returns_length_of_list_if_no_missing_i_equals_num():
    result = get_different_number([0, 1, 2, 3, 4, 5, 6, 7, 8])
    assert result == 9


def test_returns_zero_if_empty_list():
    result = get_different_number([])
    assert result == 0
