from knapsack import knapsack


def test_handles_three_weights():
    weights = [10, 20, 30]
    values = [60, 100, 120]
    capacity = 50
    assert knapsack(weights, values, capacity) == 220


def test_handles_empty_lists():
    weights = []
    values = []
    capacity = 100
    assert knapsack(weights, values, capacity) == 0
