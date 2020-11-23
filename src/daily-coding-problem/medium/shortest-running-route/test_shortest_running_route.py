from shortest_running_route import find_shortest_route
import unittest

paths = {
    (0, 1): 10,
    (0, 2): 8,
    (0, 3): 15,
    (1, 3): 12,
    (2, 4): 10,
    (3, 4): 5,
    (3, 0): 17,
    (4, 0): 10
}

class TestFindShortestRoute(unittest.TestCase):
    def test_raises_typerror(self):
        """Raises new TypeError if the argument is not of type dict"""
        def result(): return find_shortest_route("test")
        self.assertRaises(TypeError, result)

    def test_returns_none(self):
        """Returns None if the dictionary has no values"""
        result = find_shortest_route({})
        self.assertIsNone(result)
    
    def test_returns_correct_long_route(self):
        """Returns the correct long route for a runner's running route"""
        result = find_shortest_route(paths)
        self.assertEqual(result, ("0 -> 2 -> 4 -> 0", 28))


if __name__ == "__main__":
    unittest.main()