from meeting_rooms_ii import minMeetingRooms, Interval
from typing import List
import unittest


def create_interval_list(intervals: List[List[int]]) -> List[Interval]:
    return [Interval(start, end) for start, end in intervals]


class TestGetMinimuMeetingRoomsCount(unittest.TestCase):
    def test_gets_minimum_count_for_overlapping(self):
        """Takes in a list with two overlapping meetings and returns correct count"""
        result = minMeetingRooms(create_interval_list([[1, 5], [4, 9]]))
        self.assertEqual(result, 2)

    def test_gets_count_for_one_meeting_room(self):
        """Takes in a list with no overlapping meetings and returns 1"""
        result = minMeetingRooms(create_interval_list([[1, 5], [6, 9], [10, 11]]))
        self.assertEqual(result, 1)

    def test_returns_zero_if_no_meetings(self):
        """Takes in an empty meetings list and returns 0"""
        result = minMeetingRooms([])
        self.assertEqual(result, 0)

    def test_handles_small_amount_of_overlapping_meetings(self):
        """Takes in a small list of overlapping meetings and returns correct day count"""
        result = minMeetingRooms(create_interval_list([[0, 30], [5, 10], [15, 20]]))
        self.assertEqual(result, 2)

    def test_handles_large_amount_of_overlapping_meetings(self):
        """Takes in a large list of overlapping meetings and returns correct day count"""
        result = minMeetingRooms(
            create_interval_list([[1, 40], [3, 10], [5, 15], [20, 41], [44, 45]])
        )
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
