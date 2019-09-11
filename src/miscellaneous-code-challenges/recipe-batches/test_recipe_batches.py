import unittest
from recipe_batches import recipe_batches


class Test(unittest.TestCase):
    def test_recipe_batches(self):
        self.assertEqual(recipe_batches({"milk": 100, "flour": 200, "eggs": 5}, {
                         "milk": 200, "flour": 400, "eggs": 15}), 2)
        self.assertEqual(recipe_batches({}, {}), None)
        self.assertEqual(recipe_batches({'milk': 100, 'butter': 50, 'flour': 5}, {
                         'milk': 132, 'butter': 52, 'flour': 100}), 1)


if __name__ == "__main__":
    unittest.main()
