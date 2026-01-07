from partition_labels import partitionLabels


def test_partitionLabels():
    assert partitionLabels("ababcbacadefegdehijhklij") == [9, 7, 8]
    assert partitionLabels("eccbbbbdec") == [10]
    assert partitionLabels("abc") == [1, 1, 1]
    assert partitionLabels("a") == [1]
    assert partitionLabels("") == []
