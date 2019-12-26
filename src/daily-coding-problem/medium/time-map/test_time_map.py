from time_map import TimeMap
import unittest


class TestTimeMap(unittest.TestCase):
    def test_instantiates(self):
        """
        Instantiates a new copy of the TimeMap class
        """
        result = TimeMap()
        self.assertIsInstance(result, TimeMap)

    def test_adds_information_to_map(self):
        """
        Adds a key, value, and time set to self._map
        """
        time_map = TimeMap()
        time_map.set("test", "test", 5)
        result_one = time_map.values()
        self.assertEqual(result_one, {"test": {"_value": "test", "_time": 5}})
        time_map.set("test2", "test2", 100)
        result_two = time_map.values()
        self.assertEqual(result_two, {"test": {"_value": "test", "_time": 5}, "test2": {
                         "_value": "test2", "_time": 100}})

    def test_get_value_before_time(self):
        """
        Returns None if the time argument is lesser-than the
        stored key-value pair _time value
        """
        time_map = TimeMap()
        time_map.set("test", "test", 5)
        result = time_map.get("test", 1)
        self.assertEqual(result, None)

    def test_get_value_after_time(self):
        """
        Returns the value if the time argument is greater-than
        the stored key-value pair _time value
        """
        time_map = TimeMap()
        time_map.set("test", "test", 5)
        result = time_map.get("test", 10)
        self.assertEqual(result, "test")

    def test_get_value_after_overwrite(self):
        """
        Returns a new value after a key-value pair has been
        overwritten
        """
        time_map = TimeMap()
        time_map.set("test", "test", 5)
        result = time_map.get("test", 10)
        self.assertEqual(result, "test")
        time_map.set("test", "changed", 111)
        result = time_map.get("test", 500)
        self.assertEqual(result, "changed")

    def test_delete_from_map(self):
        """
        Removes a given key-value pair from self._map
        """
        time_map = TimeMap()
        time_map.set("test", "test", 10)
        time_map.delete("test")
        result = time_map.values()
        self.assertEqual(result, {})


if __name__ == "__main__":
    unittest.main()
