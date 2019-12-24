from sum_of_parts import sum_pairs
import unittest


class TestSumPairs(unittest.TestCase):
    def test_returns_none_if_not_possible(self):
        """
        Tests that None is returned if the sum cannot be found
        from any two numbers in the list
        """
        result = sum_pairs([1, 2, 3, 4], 100)
        self.assertEqual(result, None)

    def test_works_with_short_list(self):
        """
        Tests that a list is returned containing the first two integers
        that equal the second value argument for a short list
        """
        l = [1, 5, 8, 2, -10, 6, -125637, 17983, 45]
        result = sum_pairs(l, -125636)
        self.assertEqual(result, [1, -125637])

    def test_works_with_large_list(self):
        """
        Tests that a list is returned containing the first two integers
        that equal the second value argument for a large list
        """
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9, 1, 2, 3, 4, 5,
             6, 7, 8, 9, 1, 2, 3, 4, 5, 61, 7, 7, 8, 9]
        result = sum_pairs(l, 62)
        self.assertEqual(result, [1, 61])

    def test_returns_none_if_wrong_first_argument(self):
        """
        Tests that None is returned if the value of the first argument
        is not a list
        """
        result = sum_pairs("test", 5)
        self.assertEqual(result, None)

    def test_returns_none_if_wrong_second_argument(self):
        """
        Tests that None is returned if the value of the second argument
        is not an integer
        """
        result = sum_pairs([1, 2], "3")
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()
