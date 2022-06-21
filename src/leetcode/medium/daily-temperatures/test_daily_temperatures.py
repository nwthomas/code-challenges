from daily_temperatures import daily_temperatures
import unittest

class TestDailyTemperatures(unittest.TestCase):
    def test_handles_temp_list_of_length_1(self):
        """Takes in a temp list of length 1 and returns the correct result"""
        temps = [91]
        result = daily_temperatures(temps)
        self.assertEqual(result, [0])

    def test_handles_short_temp_list(self):
        """Takes in a short temp list and returns the correct result"""
        temps = [91, 99, 71, 23, 68, 100]
        result = daily_temperatures(temps)
        self.assertEqual(result, [1, 4, 3, 1, 1, 0])

    def test_handles_long_temp_list(self):
        """Takes in a long temp list and returns the correct result"""
        temps = [91, 99, 71, 23, 68, 50, 44, 87, 91, 100, 101, 20, 32, 33]
        result = daily_temperatures(temps)
        self.assertEqual(result, [1, 8, 5, 1, 3, 2, 1, 1, 1, 1, 0, 1, 1, 0])

    def test_returns_zeroes_for_no_larger_temps(self):
        """Takes in a list of temps that only decrease and returns all zeroes"""
        temps = [9, 8, 7, 6, 5, 4, 3, 2, 1]
        result = daily_temperatures(temps)
        self.assertEqual(result, [0, 0, 0, 0, 0, 0, 0, 0, 0])

if __name__ == "__main__":
    unittest.main()