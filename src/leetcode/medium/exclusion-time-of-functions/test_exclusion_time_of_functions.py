from exclusion_time_of_functions import exclusiveTime


def test_returns_zero_for_empty_list():
    """Takes in an empty list and returns 0"""
    result = exclusiveTime(2, ["0:start:0", "1:start:2", "1:end:5", "0:end:6"])
    assert result == [3, 4]


def test_returns_zero_for_no_functions():
    """Takes in a list of functions and returns 0"""
    result = exclusiveTime(
        1, ["0:start:0", "0:start:2", "0:end:5", "0:start:6", "0:end:6", "0:end:7"]
    )
    assert result == [8]


def test_returns_correct_time_for_multiple_functions():
    """Takes in a list of functions and returns the correct time"""
    result = exclusiveTime(
        2, ["0:start:0", "0:start:2", "0:end:5", "1:start:6", "1:end:6", "0:end:7"]
    )
    assert result == [7, 1]
