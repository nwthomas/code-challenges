from synonyms import are_sentences_equivalent
import unittest

class TestSynonyms(unittest.TestCase):
    def test_are_sentences_similar(self):
        """Checks if two sentences are similar"""
        result = are_sentences_equivalent([["young", "youthful"], ["aged", "old"]], "You're young but aged", "You're youthful but old")
        self.assertEqual(result, True)

    def test_are_sentences_not_similar(self):
        """Checks if two sentences are not similar"""
        result = are_sentences_equivalent([["young", "youthful"], ["aged", "old"]], "You're young but cool", "You're youthful but old")
        self.assertEqual(result, False)

if __name__ == "__main__":
    unittest.main()