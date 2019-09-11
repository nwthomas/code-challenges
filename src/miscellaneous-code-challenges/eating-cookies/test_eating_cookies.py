import unittest
from eating_cookies import eating_cookies


class Test(unittest.TestCase):
    def test_eating_cookies(self):
        self.assertEqual(eating_cookies(10), 274)
        self.assertEqual(eating_cookies(1), 1)
        self.assertEqual(eating_cookies(100), 180396380815100901214157639)
        self.assertEqual(eating_cookies(50), 10562230626642)


if __name__ == "__main__":
    unittest.main()
