from find_median_for_range import find_median_for_range
import unittest
import unittest.mock
from io import StringIO

int_list = [1, 2, 3, 4, 5, 6, 7, 8, 9]


class TestFindMedianForRange(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_prints_median_ints_for_odd_window(self, mock_stdout):
        find_median_for_range(int_list, 3)
        self.assertEqual(mock_stdout.getvalue(), "2\n3\n4\n5\n6\n7\n")

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_prints_median_ints_for_even_window(self, mock_stdout):
        find_median_for_range(int_list, 4)
        self.assertEqual(mock_stdout.getvalue(), "2.5\n3.5\n4.5\n5.5\n6.5\n")


if __name__ == "__main__":
    unittest.main()
