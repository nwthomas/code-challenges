from network_delay_time import networkDelayTime


def test_returns_negative_one_for_incomplete_connections():
    times = [[1, 2, 1]]
    n = 2
    k = 2
    assert networkDelayTime(times, n, k) == -1


def test_returns_correct_delay_for_small_graph():
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    assert networkDelayTime(times, n, k) == 2


def test_returns_correct_delay_for_large_graph():
    times = [
        [1, 2, 4],
        [1, 3, 2],
        [1, 4, 7],
        [2, 3, 1],
        [2, 5, 3],
        [2, 6, 8],
        [3, 4, 2],
        [3, 5, 6],
        [3, 7, 5],
        [4, 5, 1],
        [4, 8, 4],
        [5, 6, 2],
        [5, 7, 3],
        [5, 9, 7],
        [6, 7, 1],
        [6, 10, 5],
        [7, 8, 2],
        [7, 9, 4],
        [7, 11, 6],
        [8, 9, 1],
        [8, 12, 5],
        [9, 10, 2],
        [9, 13, 4],
        [10, 11, 3],
        [10, 14, 6],
        [11, 12, 2],
        [12, 13, 3],
        [13, 15, 5],
        [14, 15, 2],
    ]
    n = 15
    k = 1
    assert networkDelayTime(times, n, k) == 18
