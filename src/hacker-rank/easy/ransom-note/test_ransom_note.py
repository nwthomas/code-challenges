from ransom_note import check_magazine
import unittest
import unittest.mock
from io import StringIO

class TestCheckMagazine(unittest.TestCase):
    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_prints_yes(self, mock_stdout):
        """Tests that Yes is printed to the console"""
        check_magazine(["test", "ready", "player", "one"], ["one", "test", "ready"])
        self.assertEqual(mock_stdout.getvalue(), "Yes\n")

    @unittest.mock.patch('sys.stdout', new_callable=StringIO)
    def test_prints_no(self, mock_stdout):
        """Tests that No is printed to the console"""
        check_magazine(["test", "ready", "player", "one"], ["One", "Test", "Ready", "Test"])
        self.assertEqual(mock_stdout.getvalue(), "No\n")

if __name__ == "__main__":
    unittest.main()