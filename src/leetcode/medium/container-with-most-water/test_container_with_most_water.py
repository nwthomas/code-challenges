from container_with_most_water import max_area
import unittest

class TestMaxArea(unittest.TestCase):
    def test_returns_zero_for_no_max_area(self):
        """Takes in an empty array of heights and returns zero"""
        result = max_area([])
        self.assertEqual(result, 0)

    def test_returns_height_for_max_area(self):
        result = max_area([10, 4, 3, 9, 100, 2, 1, 1, 1, 5])
        self.assertEqual(result, 45)

if __name__ == "__main__":
    unittest.main()