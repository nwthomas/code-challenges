from interleave_two_queue import interleave_list
import unittest


class TestInterleaveTwoQueue(unittest.TestCase):
    def test_raises_typeerror(self):
        """
        Raises a new TypeError when the argument input is not a list
        """
        def result(): return interleave_list("test")
        self.assertRaises(TypeError, result)

    def test_returns_list_less_than_2(self):
        """
        Returns the input argument list if the length is lesser-than-or-equal-to 2
        """
        result = interleave_list([1, 4])
        self.assertEqual(result, [1, 4])

    def test_interleaves_even_length_list(self):
        """
        Correctly interleaves an even-numbered length list together
        """
        result = interleave_list([1, 5, 2, 4, 3, 10])
        self.assertEqual(result, [1, 10, 5, 3, 2, 4])

    def test_interleaves_odd_length_list(self):
        """
        Correctly interleaves an odd-numbered length list together
        """
        result = interleave_list([4, 8, 1, 3, 0, 9, 12, 3, 5])
        self.assertEqual(result, [4, 5, 8, 3, 1, 12, 3, 9, 0])


if __name__ == "__main__":
    unittest.main()
