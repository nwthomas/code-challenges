from spreadsheet import Spreadsheet
import unittest

class TestSpreadsheet(unittest.TestCase):
    def test_returns_expected_value(self):
        """Returns the expected value from the spreadsheet's cells"""
        spreadsheet = Spreadsheet()
        spreadsheet.put("test", "=test2+90")
        spreadsheet.put("test2", "=90+90")
        print(spreadsheet.get("test"))

if __name__ == "__main__":
    unittest.main()