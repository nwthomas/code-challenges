from last_prisoner_alive import get_last_alive_prisoner
import unittest

class TestGetLastPrisonerAlive(unittest.TestCase):
    def test_returns_correct_position_short_list_low_index(self):
        """Returns correct index of last position in short length of prisoners with low index"""
        result = get_last_alive_prisoner(5, 2)
        self.assertEqual(result, 3)

    def test_returns_correct_position_long_list_low_index(self):
        """Returns correct index for last position in long length of prisoners"""
        result = get_last_alive_prisoner(10, 3)
        self.assertEqual(result, 4)

    def test_returns_correct_position_short_list_large_index(self):
        """Returns correct index for short list with a large index"""
        result = get_last_alive_prisoner(5, 6)
        self.assertEqual(result, 3)

    def test_returns_correct_position_long_list_long_index(self):
        """Returns correct index for long list with a large index"""
        result = get_last_alive_prisoner(20, 10)
        self.assertEqual(result, 14)


if __name__ == "__main__":
    unittest.main()