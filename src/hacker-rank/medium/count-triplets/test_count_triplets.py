from count_triplets import countTriplets as count_triplets
import unittest

class TestCountTriplets(unittest.TestCase):
    def test_returns_correct_count_small_array(self):
        """Takes in an small array of ascending values with the r vase geometric
        progression value and returns the triplet count
        """
        result = count_triplets([1, 2, 2, 4], 2)
        self.assertEqual(result, 2)

    def test_returns_correct_count_large_array(self):
        """Takes in a large array of ascending values with the r base geometric
        progression value and returns the triplet count
        """
        result = count_triplets([1, 3, 5, 9, 9, 27, 81], 3)
        self.assertEqual(result, 6)
    
    def test_returns_correct_count_empty_array(self):
        """Returns 0 if the array is empty"""
        result = count_triplets([], 10)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()