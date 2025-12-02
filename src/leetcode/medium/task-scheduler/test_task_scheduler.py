from task_scheduler import leastInterval
import unittest


class TestLeastInterval(unittest.TestCase):
    def test_returns_correct_interval(self):
        """Takes in a list of tasks and an integer and returns the correct interval"""
        result = leastInterval(["A", "A", "A", "B", "B", "B"], 2)
        self.assertEqual(result, 8)

    def test_returns_correct_interval_for_long_list(self):
        """Takes in a long list of tasks and an integer and returns the correct interval"""
        result = leastInterval(
            [
                "A",
                "A",
                "A",
                "B",
                "B",
                "B",
            ],
            2,
        )
        self.assertEqual(result, 8)

    def test_returns_correct_interval_for_no_tasks(self):
        """Takes in a list of tasks and an integer and returns the correct interval"""
        result = leastInterval([], 2)
        self.assertEqual(result, 0)


if __name__ == "__main__":
    unittest.main()
