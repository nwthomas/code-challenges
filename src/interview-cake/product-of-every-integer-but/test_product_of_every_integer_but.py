from product_of_every_integer_but import get_products_of_all_ints_except_at_index
import unittest


class TestGetProductsOfAllIntsExceptAtIndex(unittest.TestCase):
    def test_raises_typeerror_if_argument_is_not_list(self):
        """Raises a new TypeError if the argument is not of type list"""
        def result(): get_products_of_all_ints_except_at_index("test")
        self.assertRaises(TypeError, result)

    def test_raises_exception_for_empty_list(self):
        """Raises an exception if the argument is []"""
        def result(): get_products_of_all_ints_except_at_index([])
        self.assertRaises(Exception, result)

    def test_raises_exception_for_list_of_length_one(self):
        """Raises a new error if the length of the list is 1"""
        def result(): get_products_of_all_ints_except_at_index([1])
        self.assertRaises(Exception, result)

    def test_returns_result_for_list_of_len_two(self):
        """Returns the correct result for a list of length 2"""
        self.assertEqual(
            get_products_of_all_ints_except_at_index([3, 10]), [10, 3])

    def test_returns_result_for_list_of_ints(self):
        """Returns the correct result for a long list of integers"""
        int_list = [1, 4, 7, 2, 3]
        result = get_products_of_all_ints_except_at_index(int_list)
        self.assertEqual(result, [168, 42, 24, 84, 56])


if __name__ == "__main__":
    unittest.main()
