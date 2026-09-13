from sentence_similarity import areSentencesSimilar


def test_are_sentences_similar():
    sentencel = ["Let's", "code", "in", "Python"]
    sentence2 = ["Let's", "program", "in", "Python"]
    similarPairs = [("code", "program")]
    result = areSentencesSimilar(sentencel, sentence2, similarPairs)
    assert result


def test_sentences_arent_similar():
    sentencel = ["I", "love", "to", "play", "football"]
    sentence2 = ["I", "love", "playing", "soccer"]
    similarPairs = [("play", "playing"), ("football", "soccer")]
    result = areSentencesSimilar(sentencel, sentence2, similarPairs)
    assert not result


def test_returns_false_with_unequal_sentences_length():
    sentencel = ["I", "love", "to", "play"]
    sentence2 = ["I", "love", "playing", "soccer"]
    similarPairs = [("play", "playing"), ("football", "soccer")]
    result = areSentencesSimilar(sentencel, sentence2, similarPairs)
    assert not result


def test_returns_true_multiple_edge_traversal():
    sentencel = ["Let's", "code", "in", "Python"]
    sentence2 = ["Let's", "program", "in", "Python"]
    similarPairs = [("code", "play"), ("play", "type"), ("type", "program")]
    result = areSentencesSimilar(sentencel, sentence2, similarPairs)
    assert result
