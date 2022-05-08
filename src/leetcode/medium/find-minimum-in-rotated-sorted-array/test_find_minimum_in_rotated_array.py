from find_minimum_in_rotated_array import find_min
import unittest

class TestFindMin(unittest.TestCase):
    def test_returns_min_with_list_length_one(self):
        """Takes in an array of length 1 and returns the value"""
        result = find_min([777])
        self.assertEqual(result, 777)

    def test_returns_min_with_list_length_two(self):
        """Takes in an array of length 2 and returns the value"""
        result = find_min([4, 17])
        self.assertEqual(result, 4)

    def test_returns_min_with_rotated_array(self):
        """Takes in a rotated array and returns the minimum value"""
        result = find_min([6, 7, 8, 9, 0, 1, 2, 3, 4, 5])
        self.assertEqual(result, 0)

    def test_returns_min_with_not_rotated_array(self):
        """Takes in a non-rotated array and returns the minimum value"""
        result = find_min([4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 50, 60, 10000000])
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()