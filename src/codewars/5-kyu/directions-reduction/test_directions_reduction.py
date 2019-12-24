from directions_reduction import reduce_directions
import unittest


class TestReduceDirections(unittest.TestCase):
    def test_returns_empty(self):
        """
        Returns an empty list if an empty list of directions is passed in
        """
        result = reduce_directions([])
        self.assertEqual(result, [])

    def test_handles_bad_arguments(self):
        """
        Returns an empty list if the argument passed in is not a list
        """
        result = reduce_directions("test")
        self.assertEqual(result, [])

    def test_handles_short_direction_list(self):
        """
        Returns the correct final directions for a short list
        """
        l = ["EAST", "WEST", "NORTH", "SOUTH", "WEST"]
        result = reduce_directions(l)
        self.assertEqual(result, ["WEST"])

    def test_handles_long_direction_list(self):
        """
        Returns the correct final directions for a long list
        """
        l = ["NORTH", "EAST", "WEST", "SOUTH", "EAST", "WEST", "NORTH",
             "EAST", "EAST", "WEST", "WEST", "SOUTH", "WEST", "NORTH"]
        result = reduce_directions(l)
        self.assertEqual(result, ["WEST", "NORTH"])


if __name__ == "__main__":
    unittest.main()
