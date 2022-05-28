from jump_game_ii import can_jump
import unittest

class TestCanJump(unittest.TestCase):
    def test_returns_correct_jump_for_short_list(self):
        """Returns the correct minimum number of jumps for a short list"""
        result = can_jump([3, 1, 1, 2, 6, 3])
        self.assertEqual(result, 2)

    def test_returns_correct_jumps_for_long_list(self):
        """Returns the correct minimum number of jumps for a long list"""
        result = can_jump([5, 1, 1, 1, 1, 1, 1, 1, 7, 2, 3, 2, 1, 1, 3, 0, 5, 5, 1, 1, 1, 1, 1])
        self.assertEqual(result, 7)


if __name__ == "__main__":
    unittest.main()