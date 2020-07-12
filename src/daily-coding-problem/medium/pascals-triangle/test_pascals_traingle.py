from pascals_triangle import find_pascals_triangle_row
import unittest


class TestPascalsTriangle(unittest.TestCase):
    def test_throws_type_error(self):
        """
        Raises an exception of TypeError when a non-int is given as an argument
        """
        def result(): return find_pascals_triangle_row({"test": "test"})
        self.assertRaises(TypeError, result)

    def test_returns_correct_row_1(self):
        """
        Returns the correct row for k = 1, which is [1]
        """
        result = find_pascals_triangle_row(1)
        self.assertEqual(result, [1])

    def test_returns_correct_row_2(self):
        """
        Returns the correct row for k = 2, which is [1, 1]
        """
        result = find_pascals_triangle_row(2)
        self.assertEqual(result, [1, 1])

    def test_returns_correct_row_3(self):
        """
        Returns the correct row for k = 3, which is [1, 2, 1]
        """
        result = find_pascals_triangle_row(3)
        self.assertEqual(result, [1, 2, 1])

    def test_returns_correct_medium_sized_row(self):
        """
        Returns the correct row for k = 10, which is [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
        """
        result = find_pascals_triangle_row(10)
        self.assertEqual(result, [1, 9, 36, 84, 126, 126, 84, 36, 9, 1])

    def test_returns_correct_large_sized_row(self):
        """
        Returns the correct row for k = 30, which is:

        [1,
        29,
        406,
        3654,
        23751,
        118755,
        475020,
        1560780,
        4292145,
        10015005,
        20030010,
        34597290,
        51895935,
        67863915,
        77558760,
        77558760,
        67863915,
        51895935,
        34597290,
        20030010,
        10015005,
        4292145,
        1560780,
        475020,
        118755,
        23751,
        3654,
        406,
        29,
        1]
        """
        result = find_pascals_triangle_row(30)
        self.assertEqual(result, [1,
                                  29,
                                  406,
                                  3654,
                                  23751,
                                  118755,
                                  475020,
                                  1560780,
                                  4292145,
                                  10015005,
                                  20030010,
                                  34597290,
                                  51895935,
                                  67863915,
                                  77558760,
                                  77558760,
                                  67863915,
                                  51895935,
                                  34597290,
                                  20030010,
                                  10015005,
                                  4292145,
                                  1560780,
                                  475020,
                                  118755,
                                  23751,
                                  3654,
                                  406,
                                  29,
                                  1])


if __name__ == "__main__":
    unittest.main()
