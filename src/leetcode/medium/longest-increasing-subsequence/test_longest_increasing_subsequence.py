from longest_increasing_subsequence import get_longest_increasing_subsequence
import unittest

class TestGetLongestIncreasingSubsequence(unittest.TestCase):
    def test_returns_one_for_no_increasing_subsequence(self):
        """Returns one if there are no increasing subsequences"""
        result = get_longest_increasing_subsequence([9, 8, 7, 6, 5, 4, 3, 2, 1])
        self.assertEqual(result, 1)

    def test_returns_correct_increasing_subsequence_total(self):
        """Takes in a list of numbers and returns the longest increasing subsequence"""
        result = get_longest_increasing_subsequence([3, 2, 5, 6, 9, 1, 10, 3, 15])
        self.assertEqual(result, 6)

    def test_raises_exception_if_inputted_argument_is_not_list(self):
        """Raises a new TypeError exception if inputted argument is not a list"""
        def result():
            return get_longest_increasing_subsequence(12345)
        
        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()