from longest_increasing_subsequence import get_longest_increasing_subsequence


def test_returns_one_for_no_increasing_subsequence():
    result = get_longest_increasing_subsequence(
        [9, 8, 7, 6, 5, 4, 3, 2, 1])
    assert result == 1


def test_returns_correct_increasing_subsequence_total():
    result = get_longest_increasing_subsequence(
        [3, 2, 5, 6, 9, 1, 10, 3, 15])
    assert result == 6
