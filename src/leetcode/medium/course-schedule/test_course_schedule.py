from course_schedule import can_finish_courses
import unittest

class TestCanFinishCourses(unittest.TestCase):
    def test_returns_true_if_no_prereqs(self):
        """Takes in a number of courses and empty list of prereqs and returns True"""
        result = can_finish_courses(100, [])
        self.assertTrue(result)

    def test_returns_false_if_courses_are_not_possible(self):
        """Takes in a number of courses and an impossible prereq list and returns False"""
        result = can_finish_courses(1000, [[0, 1], [5, 100], [100, 3], [1, 0]])
        self.assertFalse(result)

    def test_returns_true_if_courses_are_possible(self):
        """Takes in a number of courses and a possible prereq list and returns True"""
        result = can_finish_courses(20, [[0,10],[3,18],[5,10],[6,11],[11,14],[13,1],[15,1],[17,4]])
        self.assertTrue(result)

if __name__ == "__main__":
    unittest.main()