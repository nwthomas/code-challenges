from time_based_key_value_store import TimeMap
import unittest

class TestTimeMap(unittest.TestCase):
    def test_adds_values_to_map(self):
        """Adds a value to the map"""
        time_map = TimeMap()
        time_map.set("test", "test", 1)
        result = time_map.get("test", 1)
        self.assertEqual(result, "test")

    def test_returns_empty_string_if_no_value_is_found(self):
        """Returns an empty string if no value is found"""
        time_map = TimeMap()
        result = time_map.get("test", 1)
        self.assertEqual(result, "")

    def test_returns_correct_value_if_multiple_values_are_set(self):
        """Returns the correct values at different timestamp"""
        time_map = TimeMap()
        time_map.set("test", "test", 1)
        time_map.set("test", "test2", 2)
        result = time_map.get("test", 1)
        self.assertEqual(result, "test")
        result = time_map.get("test", 2)
        self.assertEqual(result, "test2")

    def test_returns_correct_value_for_different_keys(self):
        """Returns the correct value for different keys"""
        time_map = TimeMap()
        time_map.set("test", "test", 1)
        time_map.set("test2", "test2", 2)
        result = time_map.get("test", 1)
        self.assertEqual(result, "test")
        result = time_map.get("test2", 2)
        self.assertEqual(result, "test2")

    def test_returns_correct_value_for_same_key_at_different_timestamps(self):
        """Returns the correct value for same key at different timestamps"""
        time_map = TimeMap()
        time_map.set("test", "test", 1)
        time_map.set("test", "test2", 2)
        time_map.set("test", "test3", 100)
        time_map.get("test", 0)
        result = time_map.get("test", 0)
        self.assertEqual(result, "")
        result = time_map.get("test", 1)
        self.assertEqual(result, "test")
        result = time_map.get("test", 2)
        self.assertEqual(result, "test2")
        result = time_map.get("test", 50)
        self.assertEqual(result, "test2")
        result = time_map.get("test", 100)
        self.assertEqual(result, "test3")
        result = time_map.get("test", 101)
        self.assertEqual(result, "test3")

    def test_returns_correct_value_for_different_keys_at_different_timestamps(self):
        """Returns the correct value for different keys at different timestamps"""
        time_map = TimeMap()
        time_map.set("test", "test", 1)
        time_map.set("test2", "test2", 2)
        result = time_map.get("test", 1)
if __name__ == "__main__":
    unittest.main()