from maximum_subarray import maxSubArray


def test_array_of_length_one():
    result = maxSubArray([10])
    assert result == 10


def test_short_array():
    result = maxSubArray([1, 4, 28, -100, 4, 40, 13])
    assert result == 57


def test_long_array():
    result = maxSubArray([
        1, 4, 28, -100, 4, 40, 13, 1000,
        -200, -400, 500, 3, -20, -300, 100,
    ])
    assert result == 1057
