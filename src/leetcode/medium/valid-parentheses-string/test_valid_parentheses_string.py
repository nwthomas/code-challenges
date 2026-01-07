from valid_parentheses_string import checkValidString


def test_check_valid_string():
    assert checkValidString("()") == True
    assert checkValidString("(*)") == True
    assert checkValidString("(*))") == True
    assert checkValidString("(") == False
    assert checkValidString(")") == False
    assert checkValidString("*") == True
    assert checkValidString("*****") == True
    assert checkValidString("((*()))(*(*((*))))") == True
