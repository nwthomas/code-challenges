from quxes_island import get_smallest_quxes_number
import unittest

class TestGetSmallestQuxesNumber(unittest.TestCase):
    def test_handles_short_list_of_quxes(self):
        """Takes in a short list of quxes and returns the minimum with flipping them"""
        result = get_smallest_quxes_number(["R", "B", "G"])
        self.assertEqual(result, ["G", "G"])

    def test_handles_long_list_of_quxes(self):
        """Takes in a long list of quxes and returns the minimum with flipping them"""
        l = ["R", "G", "G", "B", "R", "B", "G", "G", "R"]
        result = get_smallest_quxes_number(l)
        self.assertEqual(result, ["R"])

if __name__ == "__main__":
    unittest.main()