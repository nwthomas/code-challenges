from shortest_word_edit_path import shortestWordEditPath


def test_edits_between_moderate_distance():
    source = "bit"
    target = "dog"
    words = ["but", "put", "big", "pot", "pog", "dog", "lot"]
    result = shortestWordEditPath(source, target, words)
    assert result == 5


def test_returns_negative_one_for_noe_path():
    source = "no"
    target = "go"
    words = ["to"]
    result = shortestWordEditPath(source, target, words)
    assert result == -1
