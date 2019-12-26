from snail import snail
import unittest


class TestSnail(unittest.TestCase):
    def test_snail_sort_small_list(self):
        """
        Tests that the snail sort algorithm returns a small list path
        sorted in winding snail order
        """
        l = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
        result = snail(l)
        self.assertEqual(result, [1, 2, 3, 6, 9, 8, 7, 4, 5])

    def test_snail_sort_large_list(self):
        """
        Tests that the snail sort alrogrithm returns a large list path
        sorted in winding snail order
        """
        l = [[3, 78, 45, 12, 5, 3], [7, 4, 345, 76, 12, 4], [0, 0, 0, 0, 0, 0], [
            5456, 123, 6345, 123, 5435, 1], [1, 2, 3, 4, 5, 6], [678, 45, 12, 54, 123, 2]]
        result = snail(l)
        self.assertEqual(result, [3, 78, 45, 12, 5, 3, 4, 0, 1, 6, 2, 123, 54, 12, 45, 678,
                                  1, 5456, 0, 7, 4, 345, 76, 12, 0, 5435, 5, 4, 3, 2, 123, 0, 0, 0, 123, 6345])

    def test_handles_assorted_data_types(self):
        """
        Tests that the snail sort alrogrithm can handle other data types
        than just integers
        """
        l = [["1", {}, [], 45], ["string", None, None, {"test": "test"}],
             [[1, 2, 3, 4], 2, 3, 4], [4.55, 6.22, "test", ""]]
        result = snail(l)
        self.assertEqual(result, ["1", {}, [], 45, {"test": "test"}, 4, "", "test", 6.22, 4.55, [
                         1, 2, 3, 4], "string", None, None, 3, 2])


if __name__ == "__main__":
    unittest.main()
