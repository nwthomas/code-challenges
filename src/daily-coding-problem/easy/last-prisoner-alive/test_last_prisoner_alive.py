from last_prisoner_alive import get_last_alive_prisoner
import unittest

class TestGetLastPrisonerAlive(unittest.TestCase):
    def test_returns_correct_position_for_short_list(self):
        """Returns correct index of last position in short length of prisoners"""
        result = get_last_alive_prisoner(5, 2)
        self.assertEqual(result, 3)

    def test_returns_correct_position_for_long_list(self):
        """Returns correct index for last position in long length of prisoners"""
        result = get_last_alive_prisoner(10, 3)
        self.assertEqual(result, 3)

if __name__ == "__main__":
    unittest.main()