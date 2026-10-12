import pytest
from course_schedule_ii import findOrder


@pytest.mark.parametrize(
    "num_courses, prerequisites, expected",
    [
        pytest.param(
            2,
            [[1, 0]],
            [0, 1],
            id="short-list",
        ),
        pytest.param(
            20,
            [
                [0, 10],
                [3, 18],
                [5, 10],
                [6, 11],
                [11, 14],
                [13, 1],
                [15, 1],
                [17, 4],
            ],
            [
                10, 0, 1, 2, 18, 3, 4, 5, 14, 11,
                6, 7, 8, 9, 12, 13, 15, 16, 17, 19,
            ],
            id="long-list",
        ),
        pytest.param(
            0,
            [],
            [],
            id="no-courses",
        ),
        pytest.param(
            2,
            [[1, 0], [0, 1]],
            [],
            id="cycle",
        ),
    ],
)
def test_find_order(num_courses, prerequisites, expected):
    assert findOrder(num_courses, prerequisites) == expected
