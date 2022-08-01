from implement_trie_prefix_tree import Trie
import unittest

class TestTrie(unittest.TestCase):
    def test_instantiates_new_trie(self):
        """Instantiates a new version of the Trie class"""
        trie = Trie()
        self.assertIsInstance(trie, Trie)

    def test_adds_word_to_trie(self):
        """Adds a new word to the Trie class"""
        trie = Trie()
        trie.insert("testing")
        trie.insert("test")

        has_word = trie.search("test")
        self.assertTrue(has_word)

        has_word = trie.search("nathan")
        self.assertFalse(has_word)

        has_word = trie.search("testing")
        self.assertTrue(has_word)

    def test_returns_true_if_any_word_with_prefix_exists(self):
        """Returns True if any word with a prefix """
        trie = Trie()
        trie.insert("testing")
        trie.insert("testify")

        has_any_word = trie.startsWith("test")
        self.assertTrue(has_any_word)

        has_any_word = trie.startsWith("tent")
        self.assertFalse(has_any_word)


if __name__ == "__main__":
    unittest.main()