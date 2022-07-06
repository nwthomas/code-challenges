from meeting_rooms import can_person_attend_all_meetings
import unittest

class TestCanPersonAttendAllMeetings(unittest.TestCase):
    def test_returns_true_if_empty_list(self):
        """Takes in an empty list and returns True"""
        result = can_person_attend_all_meetings([])
        self.assertTrue(result)

    def test_returns_true_if_one_meeting(self):
        """Takes in a list with one meeting and returns True"""
        result = can_person_attend_all_meetings([[1, 5]])
        self.assertTrue(result)

    def test_returns_true_if_no_overlapping_meetings(self):
        """Takes in a list of meetings that don't overlap and returns True"""
        result = can_person_attend_all_meetings([[1, 5], [6, 9], [10, 15]])
        self.assertTrue(result)

    def test_returns_false_for_any_overlapping_meetings(self):
        """Takes in a list with overlapping meetings and returns False"""
        result = can_person_attend_all_meetings([[3, 7], [4, 10], [11, 15]])
        self.assertFalse(result)

if __name__ == "__main__":
    unittest.main()