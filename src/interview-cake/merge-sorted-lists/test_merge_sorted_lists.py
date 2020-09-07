from merge_sorted_lists import merge_sorted_cookie_lists
import unittest


class TestMergeSortedCookieLists(unittest.TestCase):
    def test_throws_typeerror_if_first_argument_is_not_list(self):
        """Throws TypeError if the first argument is not of type list"""
        def result(): return merge_sorted_cookie_lists("test", [1, 2, 3])
        self.assertRaises(TypeError, result)

    def test_throw_typeerror_if_second_argument_is_not_list(self):
        """Throws TypeError if the second argument is not of type list"""
        def result(): return merge_sorted_cookie_lists([1, 2, 3], "test")
        self.assertRaises(TypeError, result)

    def test_returns_first_list_if_second_list_empty(self):
        """Returns the first list if the second's length is 0"""
        result = merge_sorted_cookie_lists([1, 2, 3], [])
        self.assertEqual(result, [1, 2, 3])

    def test_returns_second_list_if_first_list_empty(self):
        """Returns the second list if the first's length is 0"""
        result = merge_sorted_cookie_lists([], [1, 3, 5, 6])
        self.assertEqual(result, [1, 3, 5, 6])

    def test_returns_empty_list_if_both_arguments_empty(self):
        """Returns an empty list if both arguments passed in are empty"""
        result = merge_sorted_cookie_lists([], [])
        self.assertEqual(result, [])

    def test_merge_two_lists_together(self):
        """Merges two lists of cookie orders together"""
        result = merge_sorted_cookie_lists([1, 5, 7, 9], [4, 6, 9, 10])
        self.assertEqual(result, [1, 4, 5, 6, 7, 9, 9, 10])


if __name__ == "__main__":
    unittest.main()
