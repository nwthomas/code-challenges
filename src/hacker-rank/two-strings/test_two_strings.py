from two_strings import do_two_strings_share_substrings
import unittest

class TestDoTwoStringsShareSubstrings(unittest.TestCase):
    def test_returns_true(self):
        result = do_two_strings_share_substrings("aaa", "cat")
        self.assertEqual(result, True)

    def test_returns_false(self):
        result = do_two_strings_share_substrings("aaa", "bbb")
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()