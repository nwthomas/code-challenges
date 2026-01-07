from jump_game import can_jump
import unittest


class TestCanJump(unittest.TestCase):
    def test_return_true_for_empty_list(self):
        """Takes in an empty list and returns true"""
        result = can_jump([])
        self.assertTrue(result)

    def test_returns_true_for_length_one(self):
        """Takes in a list of length 1 and returns True"""
        result = can_jump([0])
        self.assertTrue(result)

    def test_returns_true_for_viable_solution(self):
        """Takes in a list with a valid jump list and returns True"""
        result = can_jump([3, 1, 2, 0, 5, 3])
        self.assertTrue(result)

    def test_returns_false_for_non_viable_solution(self):
        """Takes in a list with an invalid jump list and returns False"""
        result = can_jump([5, 2, 1, 1, 1, 1, 0, 0, 7])
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
