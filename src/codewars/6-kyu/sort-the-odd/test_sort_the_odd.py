from sort_the_odd import sort_array, quick_sort
import unittest


class TestQuickSort(unittest.TestCase):
    def test_raises_typeerror_if_not_list(self):
        """Raises a new TypeError if the input argument is not of type list"""
        def result(): return quick_sort("test")
        self.assertRaises(TypeError, result)

    def test_returns_empty_list_if_arg_is_empty_list(self):
        """Returns an empty list if the argument is an empty list"""
        result = quick_sort([])
        self.assertEqual(result, [])

    def test_sorts_list_of_nums(self):
        """Quick sorts a list of numbers"""
        result = quick_sort([5, 3, 8, 2, 9])
        self.assertEqual(result, [2, 3, 5, 8, 9])


class TestSortTheOdd(unittest.TestCase):
    def test_raises_typeerror_if_not_list(self):
        """Raises a new TypeError if the input argument is not of type list"""
        def result(): return sort_array("test")
        self.assertRaises(TypeError, result)

    def test_returns_empty_list_if_arg_is_empty_list(self):
        """Returns an empty list if the argument is an empty list"""
        result = sort_array([])
        self.assertEqual(result, [])

    def test_sort_all_odd(self):
        """Sorts a list of all odd numbers"""
        result = sort_array([1, 3, 7, 5, 9])
        self.assertEqual(result, [1, 3, 5, 7, 9])

    def test_does_not_sort_all_even(self):
        """Does not modify or sort a list of all even numbers"""
        result = sort_array([4, 6, 2, 4, 10])
        self.assertEqual(result, [4, 6, 2, 4, 10])

    def test_sort_short_list_with_odd_numbers(self):
        """Sorts a short list of integers with odd numbers in it"""
        result = sort_array([4, 5, 2, 7, 3, 1, 10, 9])
        self.assertEqual(result, [4, 1, 2, 3, 5, 7, 10, 9])

    def test_sort_long_list_with_odd_nubmers(self):
        """Sorts a long list of integers with odd numbers in it"""
        result = sort_array([6, 3, 8, 1, 6, 34, 2, 98, 234, 2, 0, 19, 3, 5])
        self.assertEqual(result, [6, 1, 8, 3, 6, 34,
                                  2, 98, 234, 2, 0, 3, 5, 19])


if __name__ == "__main__":
    unittest.main()
