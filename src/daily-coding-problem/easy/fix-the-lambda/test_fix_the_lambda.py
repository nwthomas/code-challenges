from fix_the_lambda import print_ten_lambdas
import unittest


class TestFixTheLambda(unittest.TestCase):
    def test_print_ten_lambdas(self):
        """
        Tests that numbers 0-9 have been printed to the terminal
        """
        functions = [f() for f in print_ten_lambdas()]
        self.assertEqual(functions, [0, 1, 2, 3, 4, 5, 6, 7, 8, 9])


if __name__ == "__main__":
    unittest.main()
