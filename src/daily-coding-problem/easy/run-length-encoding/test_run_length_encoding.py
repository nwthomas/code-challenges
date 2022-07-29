from base64 import encode
from run_length_encoding import encode_run_length
import unittest

class TestEncodeRunLength(unittest.TestCase):
    def test_encodes_short_string(self):
        """Encodes a short string in run length style"""
        result = encode_run_length("AAABBBRYUIWW")
        self.assertEqual(result, "3A3B1R1Y1U1I2W")

    def test_encodes_long_string(self):
        """Encodes a long string in run length style"""
        result = encode_run_length("RRRRRTTEEEQQQQCSDUUIRRTTT")
        self.assertEqual(result, "5R2T3E4Q1C1S1D2U1I2R3T")

    def test_handles_one_char(self):
        """Encodes a string with a single character"""
        result = encode_run_length("R")
        self.assertEqual(result, "1R")

    def test_handles_empty_string(self):
        """Handles an empty string passed as argument"""
        result = encode_run_length("")
        self.assertEqual(result, "")

    def test_raises_error_if_arg_not_string(self):
        """Raises a new TypeError if argument is not a string"""
        def result():
            return encode_run_length([678])
        
        self.assertRaises(TypeError, result)

if __name__ == "__main__":
    unittest.main()