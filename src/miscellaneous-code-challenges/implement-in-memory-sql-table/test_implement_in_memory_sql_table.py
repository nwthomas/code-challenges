from implement_in_memory_sql_table import InMemorySQLTable


def test_returns_correct_values_for_small_table():
    table = InMemorySQLTable()
    table.query("SET row1 col1 value1")
    assert table.query("GET test1 col1") == "NULL"
    table.query("SET test1 col1 value1")
    assert table.query("GET row1 col1") == "value1"
    assert (
        table.query("SELECT col1 WHERE value=value1 ORDER BY col1 DESC") == "test1 row1"
    )
    assert (
        table.query("SELECT col1 WHERE value=value1 ORDER BY col1 ASC") == "row1 test1"
    )
    assert table.query("SELECT col1 WHERE value=value1") == "row1 test1"


def test_returns_correct_values_for_multiple_rows():
    table = InMemorySQLTable()
    table.query("SET row1 col1 value1")
    table.query("SET row2 col1 value2")
    table.query("SET row3 col1 value3")
    table.query("SET row4 col1 value1")
    table.query("SET row5 col1 value1")
    table.query("SET row6 col1 value1")
    table.query("SET row1 col2 another_value1")
    table.query("SET row2 col2 another_value2")
    table.query("SET row3 col2 another_value3")
    table.query("SET row4 col2 another_value1")
    table.query("SET row5 col2 another_value1")
    table.query("SET row6 col2 another_value1")
    assert (
        table.query("SELECT col1 WHERE value=value1 ORDER BY col1 DESC")
        == "row6 row5 row4 row1"
    )
    assert table.query("SELECT random_col1 WHERE value=value1 ORDER BY col1 ASC") == ""
    assert (
        table.query("SELECT col2 WHERE value=another_value1") == "row1 row4 row5 row6"
    )
    assert (
        table.query("SELECT col2 WHERE value=another_value1 ORDER BY col1 DESC")
        == "row6 row5 row4 row1"
    )
