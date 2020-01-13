from count_islands import island_counter
import unittest


class TestIslandCounter(unittest.TestCase):
    def test_returns_zero_if_list_is_empty(self):
        """
        Returns 0 if an empty list is passed into the function
        """
        result = island_counter([])
        self.assertEqual(result, 0)

    def test_returns_none_if_not_list(self):
        """
        Returns None if the argument is not of type list
        """
        result = island_counter("test")
        self.assertIsNone(result)

    def test_returns_none_if_not_list_of_lists(self):
        """
        Returns None if the argument is not a list of lists
        """
        result = island_counter(["test", "test", "test"])
        self.assertIsNone(result)

    def test_returns_number_of_islands_in_small_matrix(self):
        """
        Returns the correct number of islands in a small matrix
        """
        result = island_counter(
            [[0, 1, 1, 0], [0, 0, 0, 1], [0, 0, 0, 0], [1, 1, 0, 0]])
        self.assertEqual(result, 3)

    def test_returns_number_of_islands_in_large_matrix(self):
        """
        Returns the correct number of islands in a large matrix
        """
        matrix = [[1, 0, 0, 0, 0, 1],
                  [0, 1, 1, 0, 0, 1],
                  [1, 0, 1, 0, 0, 1],
                  [0, 1, 0, 0, 1, 0],
                  [0, 1, 0, 0, 0, 0],
                  [0, 0, 1, 0, 0, 0]]
        result = island_counter(matrix)
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()
