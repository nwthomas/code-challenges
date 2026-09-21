from car_fleet import carFleet


def test_works_on_one_car():
    """Returns 1 for a single car in the list"""
    result = carFleet(100, [3], [1])
    assert result == 1


def test_returns_one_group_for_progressively_slower_moving_cars():
    """Has an array of cars that progressively slower cars, causing one group at end"""
    result = carFleet(100, [0, 1, 2, 3, 4, 5], [100, 99, 98, 97, 96, 95])
    assert result == 1


def test_correctly_groups_cars():
    """Places cars into distinct groups based on speed"""
    result = carFleet(12, [10, 8, 0, 5, 3], [2, 4, 1, 1, 3])
    assert result == 3


def test_handles_empty_lists_for_cars():
    """Returns 0 if no cars exist"""
    result = carFleet(54, [], [])
    assert result == 0
