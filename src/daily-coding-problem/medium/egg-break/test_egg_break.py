from egg_break import get_egg_broken_floor
import unittest

class TestGetEggBrokenFloor(unittest.TestCase):
    def test_get_base_case_one_egg(self):
        result = get_egg_broken_floor(1, 5)
        self.assertEqual(result, 5)

    def test_get_base_case_one_trial(self):
        result = get_egg_broken_floor(1, 1)
        self.assertEqual(result, 1)

    def test_get_base_case_zero_floors(self):
        result = get_egg_broken_floor(0, 0)
        self.assertEqual(result, 0)

    def test_get_base_case_zero_trials(self):
        result = get_egg_broken_floor(0, 1)
        self.assertEqual(result, 0)

    def test_get_large_floor_one_trial_amount(self):
        result = get_egg_broken_floor(1, 10000)
        self.assertEqual(result, 10000)

    def test_get_large_floor_large_trial_amount(self):
        result = get_egg_broken_floor(100, 100)
        self.assertEqual(result, 7)

if __name__ == "__main__":
    unittest.main()