from remove_duplicates_in_string import identify_adjacent


def test_handles_no_adjacent():
    assert identify_adjacent("abcdef", 2) == "abcdef"


def test_handles_all_same_char():
    assert identify_adjacent("aaa", 3) == ""


def test_procedurally_removes_chars():
    assert identify_adjacent("aabbaa", 2) == ""


def test_handles_larger_string_with_no_possible_removals():
    assert identify_adjacent("aabbcc", 4) == "aabbcc"


def test_handles_larger_string_removals():
    assert identify_adjacent("pbbcggttciiippooaais", 2) == "ps"


def test_handles_empty_string():
    assert identify_adjacent("", 10) == ""
