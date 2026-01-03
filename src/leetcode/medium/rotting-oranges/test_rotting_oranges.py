from rotting_oranges import orangesRotting
import unittest


class TestOrangesRotting(unittest.TestCase):
    def test_returns_correct_minutes(self):
        """Returns the correct number of minutes for the oranges to rot"""
        self.assertEqual(orangesRotting([[2, 1, 1], [1, 1, 0], [0, 1, 1]]), 4)

    def test_returns_neg_one_if_no_oranges_can_rot(self):
        """Returns -1 if no oranges can rot"""
        self.assertEqual(orangesRotting([[2, 1, 1], [0, 1, 1], [1, 0, 1]]), -1)

    def test_returns_zero_if_no_rotten_oranges(self):
        """Returns 0 if no rotten oranges are present"""
        self.assertEqual(orangesRotting([[0, 2]]), 0)

    def test_returns_zero_if_no_oranges(self):
        """Returns 0 if no oranges are present"""
        self.assertEqual(orangesRotting([]), 0)


if __name__ == "__main__":
    unittest.main()
