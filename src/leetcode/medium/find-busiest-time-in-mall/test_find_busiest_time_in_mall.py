from find_busiest_time_in_mall import find_busiest_period


def test_returns_correct_timestamp():
    """Collates timestamps and visitors/direction together to produce busiest time"""
    output = 1487800378
    data = [[1487799425, 14, 1],
            [1487799425, 4,  0],
            [1487799425, 2,  0],
            [1487800378, 10, 1],
            [1487801478, 18, 0],
            [1487801478, 18, 1],
            [1487901013, 1,  0],
            [1487901211, 7,  1],
            [1487901211, 7,  0]]
    assert find_busiest_period(data) == output


def test_returns_none_when_no_data():
    """Returns None if there's no data input in the argument"""
    output = None
    data = []
    assert find_busiest_period(data) == output
