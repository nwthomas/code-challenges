from kth_largest_element_in_an_array import findKthLargest
import unittest

class TestKthLargestElementInAnArray(unittest.TestCase):
    def test_kth_largest_element_in_an_array(self):
        """Takes in an array of numbers and returns the kth largest element"""
        self.assertEqual(findKthLargest([3, 2, 1, 5, 6, 4], 2), 5)
        self.assertEqual(findKthLargest([3, 2, 3, 1, 2, 4, 5, 5, 6], 4), 4)

    def test_kth_largest_element_in_an_array_with_large_array(self):
        """Takes in a large array of numbers and returns the kth largest element"""
        self.assertEqual(findKthLargest([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20], 10), 11)

if __name__ == "__main__":
    unittest.main()