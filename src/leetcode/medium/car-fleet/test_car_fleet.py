from car_fleet import carFleet


def test_works_on_one_car():
    """Returns 1 for a single car in the list"""
    result = carFleet(100, [3], [1])
    assert result == 1
