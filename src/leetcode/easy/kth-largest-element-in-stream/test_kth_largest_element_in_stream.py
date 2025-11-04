from kth_largest_element_in_stream import KthLargest
import unittest

class TestKthLargest(unittest.TestCase):
    def test_kth_largest_element_in_stream(self):
        kth_largest = KthLargest(3, [4, 5, 8, 2])
        self.assertEqual(kth_largest.add(3), 4)
        self.assertEqual(kth_largest.add(5), 5)
        self.assertEqual(kth_largest.add(10), 5)
        self.assertEqual(kth_largest.add(9), 8)
        self.assertEqual(kth_largest.add(4), 8)

    def test_kth_largest_element_in_stream_with_large_stream(self):
        kth_largest = KthLargest(4, [7, 7, 7, 7, 8, 3, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20])
        self.assertEqual(kth_largest.add(2), 17)
        self.assertEqual(kth_largest.add(10), 17)
        self.assertEqual(kth_largest.add(21), 18)
        self.assertEqual(kth_largest.add(9), 18)

if __name__ == "__main__":
    unittest.main()