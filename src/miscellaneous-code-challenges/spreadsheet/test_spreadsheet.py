from spreadsheet import Spreadsheet
import unittest

class TestSpreadsheet(unittest.TestCase):
    def test_writes_expected_values(self):
        """Can write basic values successfully"""
        s = Spreadsheet()
        s.put("A1", "1");
        s.put("A2", "2");
        s.put("A3", "3");
        self.assertEqual(s.cells, { "A1": "1", "A2": "2", "A3": "3" })

    def test_writes_equations_successfully(self):
        """Can write equations successfully"""
        s = Spreadsheet()
        s.put("B1", "=A1+A2")
        s.put("B2", "=B1+2")
        s.put("B3", "=B1+B2+5")
        self.assertEqual(s.cells, {
            "B1": "=A1+A2",
            "B2": "=B1+2",
            "B3": "=B1+B2+5",
        })

    def test_gets_correct_values(self):
        """Can get the correct value from the spreadsheet"""
        s = Spreadsheet()
        s.put("A1", "1")
        self.assertEqual(s.get("A1"), 1)

    def test_gets_correct_equations_value(self):
        """Fetches the correct value for equations"""
        s = Spreadsheet()
        s.put("A1", "1")
        s.put("A2", "2")
        s.put("B1", "=A1+A2")
        self.assertEqual(s.get("B1"), 3) 

    def test_overwrites_caches_with_update_values(self):
        """Can overwrite the cached value when new key-value is put in"""
        s = Spreadsheet()
        s.put("A1", "1")
        s.put("A2", "2")
        s.put("A3", "3")
        s.put("B1", "=A1+A2")
        s.put("B2", "=B1+2")
        s.put("B3", "=B1+B2+5")
        self.assertEqual(s.get("B3"), 13)
        s.put("B2", "=4+5+A1")
        self.assertEqual(s.get("B3"), 18)

if __name__ == "__main__":
    unittest.main()