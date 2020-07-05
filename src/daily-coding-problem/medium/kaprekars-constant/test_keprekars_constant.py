from keprekars_constant import find_keprekars_constant_steps
import unittest


class TestKeprekarsConstant(unittest.TestCase):
    def test_returns_for_number(self):
        """
        Returns the number of steps required to find Keprekar's Constant
        """
        result = find_keprekars_constant_steps(9988)
        self.assertEqual(result, 4)

    def test_returns_for_small_number(self):
        """
        Returns the number of steps required to find Keprekar's Constant
        """
        result = find_keprekars_constant_steps(1234)
        self.assertEqual(result, 3)


if __name__ == "__main__":
    unittest.main()
