from matrix_iterator_class import Matrix_Iterator
import unittest

class TestMatrixIterator(unittest.TestCase):
    def test_get_next(self):
        """Gets next value from matrix"""
        iterator = Matrix_Iterator([[2, 3, 4, 5], [], [6, 7, 8, 9]])
        result = iterator.next()
        self.assertEqual(result, 2)

    def test_raises_exception_if_no_next_value(self):
        """Raises an exception if next() is called and there is no next value"""
        iterator = Matrix_Iterator([])
        
        def result():
            return iterator.next()

        self.assertRaises(Exception, result)

    def test_returns_multiple_values_on_successive_calls(self):
        """Returns multiple values each time next() is called"""
        iterator = Matrix_Iterator([[2, 3, 4, 5], [], [6, 7, 8, 9]])
        first_result = iterator.next()
        second_result = iterator.next()
        third_result = iterator.next()
        fourth_result = iterator.next()
        fifth_result = iterator.next()

        self.assertEqual(first_result, 2)
        self.assertEqual(second_result, 3)
        self.assertEqual(third_result, 4)
        self.assertEqual(fourth_result, 5)
        self.assertEqual(fifth_result, 6)

    def test_returns_multiple_values_and_then_raises_exception(self):
        """Returns multiple values and raises exception at end of matrix"""
        iterator = Matrix_Iterator([[2, 3, 4], [], [6]])
        iterator.next()
        iterator.next()
        iterator.next()
        iterator.next()

        def result():
            return iterator.next()

        self.assertRaises(Exception, result)

    def test_handles_many_empty_lists_at_start(self):
        """Returns correct value if many empty lists are at beginning of matrix"""
        iterator = Matrix_Iterator([[], [], [], [], [1, 2, 3]])
        result = iterator.next()
        self.assertEqual(result, 1)

    def test_sets_next_value_to_none(self):
        """Retrieving a value returns the value and sets next_value to None"""
        iterator = Matrix_Iterator([[2, 3, 4], [], [6]])
        iterator.has_next()

        self.assertEqual(iterator.next_value, 2)
        result = iterator.next()
        next_value = iterator.next_value
        self.assertEqual(result, 2)
        self.assertIsNone(next_value)

    def test_returns_true_for_check_for_next_value(self):
        """Returns True if has next value"""
        iterator = Matrix_Iterator([[2, 3]])
        result = iterator.has_next()
        self.assertTrue(result)

    def test_returns_false_if_not_next_value(self):
        """Returns True if has next value"""
        iterator = Matrix_Iterator([[3], [], []])
        iterator.next()
        result = iterator.has_next()
        self.assertFalse(result)

    def test_sets_next_value_when_checking_next(self):
        """Returns boolean and sets next value if it exists"""
        iterator = Matrix_Iterator([[2, 3, 4], [4], [10, 1, 4]])
        initial_next_value = iterator.next_value
        bool_result = iterator.has_next()
        final_next_value = iterator.next_value

        self.assertIsNone(initial_next_value)
        self.assertTrue(bool_result)
        self.assertEqual(final_next_value, 2)


if __name__ == "__main__":
    unittest.main()