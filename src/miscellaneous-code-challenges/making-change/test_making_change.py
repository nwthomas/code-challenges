import unittest
from making_change import making_change


class Test(unittest.TestCase):
    def test_making_change(self):
        self.assertEqual(making_change(1000, [1, 5, 10]), 10201)
        self.assertEqual(making_change(5, []), 0)
        self.assertEqual(making_change(200000, [1]), 1)
        self.assertEqual(making_change(100, [1, 25]), 5)


if __name__ == "__main__":
    unittest.main()
