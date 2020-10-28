from uglify_word import uglify_word
import unittest

class TestUglifyWord(unittest.TestCase):
    def test_uglify_short_word(self):
        result = uglify_word("nathan thomas")
        self.assertEqual(result, "NaThAn ThOmAs")
    
    def test_uglify_long_word(self):
        result = uglify_word("this is a crazy long word that doesn't make sense")
        self.assertEqual(result, "ThIs Is A CrAzY LoNg WoRd ThAt DoEsN'T MaKe SeNsE")


if __name__ == "__main__":
    unittest.main()