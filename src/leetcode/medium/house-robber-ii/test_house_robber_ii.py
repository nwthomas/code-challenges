from house_robber_ii import rob
import unittest

class TestRob(unittest.TestCase):
    def test_handles_house_list_of_length_one(self):
            """Takes in a list of houses length 1 and returns that amount"""
            houses = [9]
            result = rob(houses)
            self.assertEqual(result, 9)

    def test_handles_house_list_of_length_two(self):
        """Takes in a list of houses length 2 and returns the bigger amount"""
        houses = [1, 9]
        result = rob(houses)
        self.assertEqual(result, 9)

    def test_finds_correct_total_in_short_list_of_houses(self):
        """Takes in a short list of houses and returns the biggest amount possible"""
        houses = [1, 9, 4, 3, 6, 3, 9, 9]
        result = rob(houses)
        self.assertEqual(result, 24)

    def test_finds_correct_total_in_long_list_of_houses(self):
        """Takes in a long list of houses and returns the biggest amount possible"""
        houses = [9, 3, 5, 1, 3, 2, 5, 4, 3, 2, 7, 5, 1, 3, 5, 3]
        result = rob(houses)
        self.assertEqual(result, 38)

    def test_handles_zero_length_house_list(self):
        """Takes in a list of houses length 0 and returns 0 amount possible"""
        houses = []
        result = rob(houses)
        self.assertEqual(result, 0)

    def test_does_not_include_houses_at_end(self):
        """Takes in a list with large amount houses at each end and does not include one of them"""
        houses = [50, 4, 2, 67]
        result = rob(houses)
        self.assertEqual(result, 71)

if __name__ == "__main__":
    unittest.main()