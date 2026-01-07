from multiply_strings import multiply


def test_multiply_strings():
    assert multiply("2", "3") == "6"
    assert multiply("123", "456") == "56088"
    assert multiply("0", "0") == "0"
    assert multiply("1000000", "1000000") == "1000000000000"
    assert multiply("76512763", "127361273612736") == "9744762943309423349568"
