from os import remove
from remove_element import remove_element
import unittest

class TestRemoveElement(unittest.TestCase):
    def test_removes_in_short_array_in_place(self):
        """Takes in a short array and removes a value in place in short array"""
        array = [1, 2, 3, 3, 4, 3, 2, 3]
        remove_element(array, 3)
        self.assertEqual(array, [1, 2, 2, 4])

    def test_removes_in_long_array_in_place(self):
        """Takes in a long array and removes a value in place in a long array"""
        array = [4, 3, 6, 2, 10, 10, 4, 6, 28, 34, 2, 9, 3, 5, 4, 2, 3, 2, 3, 10]
        remove_element(array, 10)
        self.assertEqual(array, [4, 3, 6, 2, 3, 2, 4, 6, 28, 34, 2, 9, 3, 5, 4, 2, 3])

    def test_handles_all_array_of_value(self):
        """Takes in an array filled with the value to remove and ends with empty array"""
        array = [1, 1, 1, 1, 1, 1, 1, 1]
        remove_element(array, 1)
        self.assertEqual(array, [])

if __name__ == "__main__":
    unittest.main()