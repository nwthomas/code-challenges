import unittest

from group_anagrams import group_anagrams


class TestGroupAnagrams(unittest.TestCase):
    def test_properly_groups_anagrams(self):
        """Takes in a list of strings and returns a list of lists of grouped anagrams"""
        strs = ["asdf", "fdsa", "ityahjsd", "fffa", "afff"]
        result = group_anagrams(strs)
        self.assertEqual(result, [["asdf", "afff"], [
                         "fdsa", "fffa"], ["ityahjsd"]])

    def test_can_handle_empty_list(self):
        """Can properly handle an empty list and return an empty list"""
        strs = []
        result = group_anagrams(strs)
        self.assertEqual(result, [])


if __name__ == "__main__":
    unittest.main()
