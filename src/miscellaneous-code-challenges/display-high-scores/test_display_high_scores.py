from display_high_scores import sort_high_scores
import unittest


class TestSortHighScores(unittest.TestCase):
    def test_raises_type_error_if_not_list(self):
        """Raises a TypeError if the first argument is not a list"""
        def result(): return sort_high_scores({}, 100)
        self.assertRaises(TypeError, result)

    def test_raises_type_error_if_not_int(self):
        """Raises a TypeError if the second argument is not an int"""
        def result(): return sort_high_scores([1, 2, 3], "test")
        self.assertRaises(TypeError, result)

    def test_returns_sorted_list(self):
        """Returns a sorted list of high scores"""
        result = sort_high_scores([89, 40, 87, 12], 100)
        self.assertEqual(result, [89, 87, 40, 12])


if __name__ == "__main__":
    unittest.main()
