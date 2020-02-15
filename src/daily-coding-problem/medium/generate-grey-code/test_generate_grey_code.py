from generate_grey_code import find_grey_code_bits
import unittest


class TestFindGreyCodeBits(unittest.TestCase):
    def test_returns_none_if_argument_not_integer(self):
        """
        Returns None if the argument passed in is not an integer
        """
        result = find_grey_code_bits("test")
        self.assertIsNone(result)

    def test_returns_empty_list_for_argument_zero(self):
        """
        Returns an empty list if the argument is lesser-than-or-equal-to
        zero
        """
        result = find_grey_code_bits(0)
        self.assertEqual(result, [])

    def test_returns_list_for_one_bit(self):
        """
        Returns a list of ["0", "1"] for argument of 1
        """
        result = find_grey_code_bits(1)
        self.assertEqual(result, ["0", "1"])

    def test_returns_list_for_small_bit_num(self):
        """
        Returns a list of length 2 with [0, 1]
        """
        result = find_grey_code_bits(2)
        self.assertEqual(result, ["00", "01", "11", "10"])

    def test_returns_list_for_large_bit_num(self):
        """
        Returns the correct list for input integer 4
        """
        final_list = ["0000", "0001", "0011",
                      "0111", "1111", "1110", "1100", "1000"]
        result = find_grey_code_bits(4)
        self.assertEqual(result, final_list)


if __name__ == "__main__":
    unittest.main()
