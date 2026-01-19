from minimum_window_with_characters import minWindow


def test_minimum_window_with_characters():
    assert minWindow("ADOBECODEBANC", "ABC") == "BANC"
    assert minWindow("ADOBECODEBANC", "ABCDEF") == ""
    assert minWindow("ADOBECODEBANC", "") == ""
    assert minWindow("", "ABC") == ""
    assert minWindow("ADOBECODEBANC", "A") == "A"
    assert minWindow("XYABNACYAXUIAYX", "AYAX") == "ACYAX"
