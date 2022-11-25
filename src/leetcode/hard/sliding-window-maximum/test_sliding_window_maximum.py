from sliding_window_maximum import maxSlidingWindow
import unittest

class TestMaxSlidingWindow(unittest.TestCase):
    l1 = [4, 2, 0, 1, 5, 8, 2, 4, 5]
    l2 = [1, 2, 3, 1, 1, 6, 3, 2, 1]

    def test_returns_correct_value_for_list_length_one(self):
        """Takes in a list of length 1 and returns the single item"""
        result = maxSlidingWindow([10], 1)
        self.assertEqual(result, [10])

    def test_returns_correct_value_for_window_length_3(self):
        """Takes in a list with a window of length 3 and returns the maximums"""
        result = maxSlidingWindow(self.l1, 3)
        self.assertEqual(result, [4, 2, 5, 8, 8, 8, 5])

    def test_returns_correct_value_for_window_length_max(self):
        """Takes in a list with a window of length of list and returns single max"""
        result = maxSlidingWindow(self.l2, len(self.l2))
        self.assertEqual(result, [6])

if __name__ == "__main__":
    unittest.main()