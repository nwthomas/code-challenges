from number_of_connected_components import countComponents


def test_handles_small_graph_multiple_components():
    n = 5
    edges = [[0, 1], [1, 2], [3, 4]]
    assert countComponents(n, edges) == 2


def test_handles_large_graph_multiple_components():
    n = 6
    edges = [[0, 1], [1, 2], [2, 3], [3, 4]]
    assert countComponents(n, edges) == 2
