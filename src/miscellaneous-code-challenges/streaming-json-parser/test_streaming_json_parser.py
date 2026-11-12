from streaming_json_parser import parse_streaming_json


def test_parses_short_incomplete_string():
    assert parse_streaming_json('["test", ["test2", "another_test') == [
        "test", ["test2", "another_test"]]


def test_long_incomplete_nested_arrays():

    partial_json = (
        '["test", ["test2", "another_test", ["nested_string", [[[[[[[]]]], "hi"]]], "another"], "te'
    )

    result = parse_streaming_json(partial_json)
    print(result)

    assert result == ['test', ['test2', 'another_test', [
        'nested_string', [[[[[[[]]]], 'hi']]], 'another'], 'te']]


def test_complete_streaming_json():
    assert parse_streaming_json('["test", [[[], []]] ,["test2", "another_test') == [
        "test", [[[], []]], ["test2", "another_test"]]
