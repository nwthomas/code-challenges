from least_larger import least_larger
import unittest


class TestLeastLarger(unittest.TestCase):
    def test_finds_least_larger_in_small_list(self):
        """Finds the least larger number in a small list"""
        result = least_larger([3, 6, 1, 3, 4], 2)
        self.assertEqual(result, 0)

    def test_finds_least_larger_in_large_list(self):
        """Finds the least larger number in a large list"""
        result = least_larger([5, 8, 2, 5, 4, 7, 10, 8, 7, 3], 2)
        self.assertEqual(result, 9)

    def test_returns_negative_one(self):
        """Returns -1 if there is no larger number in the list"""
        result = least_larger([1, 2, 3, 4, 10, 5, 6, 7, 8, 9], 4)
        self.assertEqual(result, -1)


if __name__ == "__main__":
    unittest.main()