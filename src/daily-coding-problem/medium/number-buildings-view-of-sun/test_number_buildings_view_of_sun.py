from number_buildings_view_of_sun import find_number_buildings_view_of_sun
import unittest

class TestFindNumberBuildingsViewOfSun(unittest.TestCase):
    def test_returns_correct_number_views(self):
        """Takes in a list of apartment heights and correctly returns the total of views"""
        l = [3, 7, 8, 3, 6, 1]
        result = find_number_buildings_view_of_sun(l)
        self.assertEqual(result, 3)

    def test_returns_one_for_descending_building_heights(self):
        """Takes in a list of descending heights from sun and returns 1 for first building"""
        l = [1, 2, 3, 4, 5, 6, 7, 8, 9]
        result = find_number_buildings_view_of_sun(l)
        self.assertEqual(result, 1)

    def test_handles_no_buildings_in_list(self):
        """Handles an empty list of buildings"""
        l = []
        result = find_number_buildings_view_of_sun(l)
        self.assertEqual(result, 0)

if __name__ == "__main__":
    unittest.main()