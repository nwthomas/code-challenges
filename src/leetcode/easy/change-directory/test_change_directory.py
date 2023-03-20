from change_directory import change_directory
import unittest

class TestChangeDirectory(unittest.TestCase):
    def test_handles_empty_change_directions(self):
        result = change_directory("/t/e/s/t", "")
        self.assertEqual(result, "/t/e/s/t")

    def test_handles_initial_route_slash(self):
        """Takes in route starting with forward slash and returns change directory path"""
        result = change_directory("/t/e/s/", "/r/e/s/u/l/t")
        self.assertEqual(result, "/r/e/s/u/l/t")

    def test_handles_start_at_root_forward_slash(self):
        """Takes in / as starting route and returns it when trying to cd out"""
        result = change_directory("/", "testing/../../../..")
        self.assertEqual(result, "/")

    def test_handles_going_back_and_forwards_in_route(self):
        """Can go back part way and then forwards in returned route"""
        result = change_directory("/s/t/z/g", "h/../../../i/l")
        self.assertEqual(result, "/s/t/i/l")

if __name__ == "__main__":
    unittest.main()