from anagrams import anagrams_of
import unittest

class TestAnagramsOf(unittest.TestCase):
    def test_returns_correct_anagrams(self):
        result = anagrams_of("abc")
        self.assertEqual(result, ['abc', 'bac', 'bca', 'acb', 'cab', 'cba'])

if __name__ == "__main__":
    unittest.main()