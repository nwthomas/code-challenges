from graph_valid_tree import validTree


def test_returns_true_for_small_valid_tree():
    assert validTree(5, [
        [0, 1],
        [0, 2],
        [0, 3],
        [1, 4],
    ]) is True


def test_returns_true_for_large_valid_tree():
    assert validTree(20, [
        [0, 1],
        [1, 2],
        [2, 3],
        [3, 4],
        [0, 5],
        [5, 6],
        [6, 7],
        [7, 8],
        [8, 9],
        [9, 10],
        [10, 11],
        [11, 12],
        [12, 13],
        [13, 14],
        [14, 15],
        [15, 16],
        [16, 17],
        [17, 18],
        [18, 19],
    ]) is True


def test_returns_false_if_all_nodes_are_not_connected():
    assert validTree(3, []) is False


def test_returns_false_for_invalid_tree():
    assert validTree(5, [
        [0, 1],
        [1, 2],
        [2, 3],
        [1, 3],
        [1, 4],
    ]) is False


def test_returns_false_when_edges_form_a_loop():
    assert validTree(5, [
        [0, 1],
        [1, 0],
    ]) is False
