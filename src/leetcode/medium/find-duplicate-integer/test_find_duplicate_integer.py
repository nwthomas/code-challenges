from find_duplicate_integer import find_duplicate
import unittest

class TestFindDuplicate(unittest.TestCase):
    def test_returns_duplicate_number_in_short_array_of_nums(self):
        """Takes in a short array of numbers and returns the duplicate number"""
        result = find_duplicate([1, 3, 4, 2, 2])
        self.assertEqual(result, 2)

    def test_returns_duplicate_number_in_long_array_of_nums(self):
        """Takes in a long array of numbers and returns the duplicate number"""
        result = find_duplicate([3, 1, 4, 2, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 3])
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()