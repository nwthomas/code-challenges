from degrees_of_friendship import friend_distance


def test_returns_for_one_degree():
    matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    userA = 0
    userB = 1
    assert friend_distance(matrix, userA, userB) == 1


def test_returns_for_two_degrees():
    matrix = [[0, 1, 0], [1, 0, 1], [0, 1, 0]]
    userA = 0
    userB = 2
    assert friend_distance(matrix, userA, userB) == 2


def test_returns_for_negative_connection():
    matrix = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    userA = 0
    userB = 2
    assert friend_distance(matrix, userA, userB) == -1


def test_returns_for_longer_connection():
    matrix = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [
        0, 1, 0, 1, 0], [0, 0, 1, 0, 1], [0, 0, 0, 1, 0]]
    userA = 0
    userB = 4
    assert friend_distance(matrix, userA, userB) == 4
