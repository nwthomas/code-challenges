from synonyms import are_sentences_equivalent
import unittest

class TestSynonyms(unittest.TestCase):
    def test_are_sentences_similar(self):
        result = are_sentences_equivalent([["young", "youthful"], ["aged", "old"]], "You're young but aged", "You're youthful but old")
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()