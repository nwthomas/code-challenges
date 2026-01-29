from k_closest_points_to_origin import kClosest


def test_k_closest_points_to_origin():
    assert kClosest([[0, 2], [2, 2]], 1) == [[0, 2]]
    assert kClosest([[0, 2], [2, 0], [2, 2]], 2) == [[0, 2], [2, 0]]
    assert kClosest([[1, 3], [-2, 2]], 1) == [[-2, 2]]
    assert kClosest([[3, 3], [5, -1], [-2, 4]], 2) == [[3, 3], [-2, 4]]
    assert kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]
    assert kClosest([[1, 3], [-2, 2], [2, -2]], 2) == [[-2, 2], [2, -2]]
    assert kClosest([[0, 1], [1, 0]], 2) == [[0, 1], [1, 0]]
