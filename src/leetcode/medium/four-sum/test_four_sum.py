from four_sum import four_sum
import unittest 
from collections import defaultdict
class TestFourSum(unittest.TestCase):
    def test_returns_single_four_sum(self):
        print(four_sum([1, 0, 1, 1, 2, 2, 3, 4], 10))
        # self.assertEqual(four_sum([1, 2, 4, 5], 10), [[1, 4, 5]])
    
if __name__ == "__main__":
    unittest.main()