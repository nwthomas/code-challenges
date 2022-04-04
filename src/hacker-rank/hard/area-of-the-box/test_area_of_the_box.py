from area_of_the_box import numberOfWays
import unittest


class Tests(unittest.TestCase):
    def test_small_nums(self):
        result = numberOfWays([[3, 5], [7, 10], [1, 2]])
        self.assertEqual(result, [26, 224, 2])

    def test_mid_nums(self):
        result = numberOfWays([[1244, 687], [18632, 146427], [79, 13526]])
        self.assertEqual(result, [239951696, 24339514009400, 42660000])

    def test_large_nums(self):
        result = numberOfWays(
            [[12634687, 12364941], [816293, 871692], [8176293, 80987128]])
        self.assertEqual(
            result, [650786937644762261177, 199765479533429888, 2615966706202684349844])


if __name__ == "__main__":
    unittest.main()
