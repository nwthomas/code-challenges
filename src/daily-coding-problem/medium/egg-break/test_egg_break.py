from egg_break import get_egg_broken_floor
import unittest

class TestGetEggBrokenFloor(unittest.TestCase):
    def test_get_base_case_one_egg(self):
        result = get_egg_broken_floor(1, 10)
        self.assertEqual(result, 10)

if __name__ == "__main__":
    unittest.main()