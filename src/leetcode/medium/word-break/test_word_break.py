

from word_break import word_break


def test_successfully_breaks_words():
    words = ["leet", "code"]
    s = "leetcode"
    assert word_break(s, words)


def test_unsuccessfully_breaks_words():
    words = ["cats", "dog", "sand", "and", "cat"]
    s = "catsandog"
    assert not word_break(s, words)


def test_handles_short_string():
    words = ["dog", "s", "gs"]
    s = "dogs"
    assert word_break(s, words)
