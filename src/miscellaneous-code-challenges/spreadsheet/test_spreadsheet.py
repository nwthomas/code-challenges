from spreadsheet import Spreadsheet
import pytest


def test_writes_expected_values():
    """Can write basic values successfully"""
    s = Spreadsheet()
    s.put("A1", "1")
    s.put("A2", "2")
    s.put("A3", "3")
    assert s.cells == {"A1": "1", "A2": "2", "A3": "3"}


def test_writes_equations_successfully():
    """Can write equations successfully"""
    s = Spreadsheet()
    s.put("B1", "=A1+A2")
    s.put("B2", "=B1+2")
    s.put("B3", "=B1+B2+5")
    assert s.cells == {"B1": "=A1+A2", "B2": "=B1+2", "B3": "=B1+B2+5"}


def test_gets_correct_values():
    """Can get the correct value from the spreadsheet"""
    s = Spreadsheet()
    s.put("A1", "1")
    assert s.get("A1") == 1


def test_gets_correct_equations_value():
    """Fetches the correct value for equations"""
    s = Spreadsheet()
    s.put("A1", "1")
    s.put("A2", "2")
    s.put("B1", "=A1+A2")
    assert s.get("B1") == 3


def test_overwrites_caches_with_update_values():
    """Can overwrite the cached value when new key-value is put in"""
    s = Spreadsheet()
    s.put("A1", "1")
    s.put("A2", "2")
    s.put("A3", "3")
    s.put("B1", "=A1+A2")
    s.put("B2", "=B1+2")
    s.put("B3", "=B1+B2+5")
    assert s.get("B3") == 13
    s.put("B2", "=4+5+A1")
    assert s.get("B3") == 18


def test_raises_error_for_cycle_detection():
    """Raises an error for cycle detection"""
    s = Spreadsheet()
    s.put("A1", "=A2")
    s.put("A2", "=A1")
    with pytest.raises(ValueError):
        s.get("A1")
