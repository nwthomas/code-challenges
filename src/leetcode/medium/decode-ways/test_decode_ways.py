from decode_ways import num_decodings_iterative, num_decodings_recursive
import unittest

class TestNumDecodingsRecursive(unittest.TestCase):
    def test_handles_zero_at_beginning(self):
        """Takes in a string with 0 at the beginning and returns 0"""
        result = num_decodings_recursive("0123456789")
        self.assertEqual(result, 0)

    def test_returns_correct_count_including_zero(self):
        """Takes in a string with a zero in it and returns the correct count"""
        result = num_decodings_recursive("12109")
        self.assertEqual(result, 2)

    def test_returns_correct_count_of_long_string(self):
        """Takes in a long string containing integers and returns the correct count"""
        result = num_decodings_recursive("14129835")
        self.assertEqual(result, 4)

class TestNumDecodingsIterative(unittest.TestCase):
    def test_handles_zero_at_beginning(self):
        """Takes in a string with 0 at the beginning and returns 0"""
        result = num_decodings_iterative("0123456789")
        self.assertEqual(result, 0)

    def test_returns_correct_count_including_zero(self):
        """Takes in a string with a zero in it and returns the correct count"""
        result = num_decodings_iterative("12109")
        self.assertEqual(result, 2)

    def test_returns_correct_count_of_long_string(self):
        """Takes in a long string containing integers and returns the correct count"""
        result = num_decodings_iterative("14129835")
        self.assertEqual(result, 4)

if __name__ == "__main__":
    unittest.main()