from time_planner import meeting_planner
import unittest

class TestMeetingPlanner(unittest.TestCase):
    def test_returns_empty_list(self):
        """Takes in two empty lists and returns an empty list"""
        result = meeting_planner([], [], 1)
        self.assertEqual(result, [])

    def test_returns_empty_list_for_too_big_duration(self):
        """Takes in two lists and returns empty list"""
        result = meeting_planner([[0, 10], [15, 20]], [[3, 5], [50, 60]], 30)
        self.assertEqual(result, [])

    def test_returns_concurrent_meeting_time(self):
        """Takes in two lists and a duration and returns concurrent available time"""
        result = meeting_planner([[10, 50], [60, 120], [140, 210]], [[0, 15], [60, 70]], 8)
        self.assertEqual(result, [60, 68])

if __name__ == "__main__":
    unittest.main()