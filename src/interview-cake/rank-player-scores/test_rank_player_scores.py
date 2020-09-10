from rank_player_scores import sort_player_scores
import unittest


class TestSortPlayerScores(unittest.TestCase):
    def test_raises_typeerror_if_first_argument_not_list(self):
        """Raises a new TypeError if the first argument is not of type list"""
        def result(): return sort_player_scores({}, 100)
        self.assertRaises(TypeError, result)

    def test_raises_typeerror_if_second_argument_not_int(self):
        """Raises a new TypeError if the second argument is not of type int"""
        def result(): return sort_player_scores([1, 58, 3], "test")
        self.assertRaises(TypeError, result)

    def test_returns_empty_list_if_no_scores(self):
        """Returns an empty list if the first argument has no scores"""
        result = sort_player_scores([], 100)
        self.assertEqual(result, [])

    def test_returns_sorted_list_of_scores(self):
        """Returns a sorted list of player scores"""
        result = sort_player_scores(
            [1, 57, 3, 45, 20, 67, 8, 9, 9, 9, 3, 2], 100)
        self.assertEqual([67, 57, 45, 20, 9, 9, 9, 8, 3, 3, 2, 1], result)


if __name__ == "__main__":
    unittest.main()
