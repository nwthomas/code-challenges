from highest_multiple_of_integers import find_highest_multiple_of_three_ints
import unittest


class TestFindHighestMultipleOfThreeInts(unittest.TestCase):
    def test_finds_highest_multiple_of_three_numbers(self):
        """Finds the highest multiple of three numbers within a list of integers"""
        result = find_highest_multiple_of_three_ints([6, 3, 5, 2, 1, 10])
        self.assertEqual(result, 300)

    def test_finds_highest_with_negative_integers(self):
        """Finds the highest multiple of three numbers with negative integers present"""
        result = find_highest_multiple_of_three_ints([-100, 5, 6, 20, -9, 30])
        self.assertEqual(result, 27000)

    def test_returns_correct_product_for_list_of_three(self):
        """Returns the product of three integers in a list"""
        result = find_highest_multiple_of_three_ints([1, 2, 3])
        self.assertEqual(result, 6)

    def test_raises_typeerror_if_argument_is_not_list(self):
        """Raises a new TypeError if the argument is not of type list"""
        def result(): return find_highest_multiple_of_three_ints("test")
        self.assertRaises(TypeError, result)


if __name__ == "__main__":
    unittest.main()
