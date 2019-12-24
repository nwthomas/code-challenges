from moving_zeros_to_the_end import move_zeros
import unittest


class TestMoveZeros(unittest.TestCase):
    def test_return_none_for_wrong_argument(self):
        """
        Tests that None is returned if the array argument is wrong
        """
        result = move_zeros("test")
        self.assertEqual(result, None)

    def test_return_none_for_no_argument(self):
        """
        Tests that None is returned if no argument is passed in
        """
        result = move_zeros()
        self.assertEqual(result, None)

    def test_returns_zeros_at_end(self):
        """
        Tests that all zeros in list have been moved to the end
        """
        l = [4, 0, 9, 0, 1, 4, 0, False, None, 0, True, 0]
        result = move_zeros(l)
        self.assertEqual(result, [4, 9, 1, 4, False,
                                  None, True, 0, 0, 0, 0, 0])


if __name__ == "__main__":
    unittest.main()
