from count_squares import CountSquares


def test_count_squares():
    count_squares = CountSquares()
    count_squares.add([1, 1])
    count_squares.add([1, 2])
    count_squares.add([2, 1])
    count_squares.add([2, 2])
    count_squares.add([2, 2])
    assert count_squares.count([1, 1]) == 2
    assert count_squares.count([1, 2]) == 2
    assert count_squares.count([2, 1]) == 2
    assert count_squares.count([2, 2]) == 1
