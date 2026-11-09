from deletion_distance import deletion_distance


def test_performs_small_deletion():
    assert deletion_distance("sea", "eat") == 2


def test_performs_large_deletion():
    assert deletion_distance("leetcode", "etco") == 4


def test_handles_empty_strings():
    assert deletion_distance("test", "") == 4
