import unittest

from encode_and_decode_strings import DELIMITER, decode, encode


class TestEncodeDecode(unittest.TestCase):
    def test_encodes_string_correctly(self):
        """Correctly encodes a string"""
        strings = ["this", "is", "a", 'test']
        result = encode(strings)
        self.assertEqual(result, "4,2,1,4," + DELIMITER + "thisisatest")

    def test_decodes_string_correctly(self):
        """Correctly decodes a string"""
        string = "4,2,1,4," + DELIMITER + "thisisatest"
        result = decode(string)
        self.assertEqual(result, ["this", "is", "a", "test"])

if __name__ == "__main__":
    unittest.main()