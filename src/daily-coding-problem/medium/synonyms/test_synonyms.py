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

    def test_are_deeply_linked_synonym_sentences_similar(self):
        """Checks if two sentences are similar that are deeply linked (e.g. more than 2) in their synonyms"""
        synonyms = [["young", "youthful"], ["youthful", "lively"]]
        result = are_sentences_equivalent(synonyms, "You're young but cool", "You're lively but cool")
        self.assertEqual(result, True)

if __name__ == "__main__":
    unittest.main()