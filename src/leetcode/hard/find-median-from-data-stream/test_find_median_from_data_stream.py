from find_median_from_data_stream import MedianFinder
import unittest

class TestMedianFinder(unittest.TestCase):
    def test_finds_median_in_small_data_stream(self):
        mf = MedianFinder()
        mf.add_num(5),
        mf.add_num(10)
        first_median = mf.find_median()
        mf.add_num(3)
        second_median = mf.find_median()
        self.assertEqual(first_median, 7.5)
        self.assertEqual(second_median, 5)

    def test_finds_media_in_large_data_stream(self):
        mf = MedianFinder()

        for i in range(1000000):
            mf.add_num(i)

        median = mf.find_median()
        self.assertEqual(median, 499999.5)

if __name__ == "__main__":
    unittest.main()