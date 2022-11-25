from encode_and_decode_strings import decode, encode, ENCODING_SPACER
import unittest

class TestEncodeDecode(unittest.TestCase):
    def test_encodes_string_correctly(self):
        """Correctly encodes a string"""
        strings = ["this", "is", "a", 'test']
        result = encode(strings)
        self.assertEqual(result, "this" + ENCODING_SPACER + "is" + ENCODING_SPACER + "a" + ENCODING_SPACER + "test")

    def test_decodes_string_correctly(self):
        """Correctly decodes a string"""
        string = "this" + ENCODING_SPACER + "is" + ENCODING_SPACER + "a" + ENCODING_SPACER + "test"
        result = decode(string)
        self.assertEqual(result, ["this", "is", "a", "test"])

if __name__ == "__main__":
    unittest.main()