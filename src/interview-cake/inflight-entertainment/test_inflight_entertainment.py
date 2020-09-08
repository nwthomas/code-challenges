from inflight_entertainment import find_exact_flight_movie_runtime
import unittest


class TestFindExactFlightMovieRuntime(unittest.TestCase):
    def test_throws_typeerror_if_first_argument_is_not_int(self):
        """Throws TypeError if the first argument is not of type int"""
        def result(): return find_exact_flight_movie_runtime("test", [1, 2, 3])
        self.assertRaises(TypeError, result)

    def test_throws_typeerror_if_second_argument_is_not_list(self):
        """Throws TypeError if the second argument is not of type list"""
        def result(): return find_exact_flight_movie_runtime(60, "test")
        self.assertRaises(TypeError, result)

    def test_returns_false_if_movie_length_list_empty(self):
        """Returns a False boolean if the list of movie lengths is empty"""
        result = find_exact_flight_movie_runtime(100, [])
        self.assertFalse(result)

    def test_returns_true_if_length_combination_is_possible(self):
        """Returns a True boolean if two movies exist that match the exact flight length"""
        result = find_exact_flight_movie_runtime(100, [10, 40, 50, 30, 20, 60])
        self.assertTrue(result)

    def test_returns_false_if_length_combination_is_not_possible(self):
        """Returns a False boolean if two movies do not exist that match the exact flight length"""
        result = find_exact_flight_movie_runtime(
            100, [50, 20, 30, 10, 150, 40])
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
