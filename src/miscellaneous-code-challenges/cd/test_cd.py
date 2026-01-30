from cd import change_directory


def test_change_directory():
    assert change_directory("/foo/bar", "baz") == "/foo/bar/baz"
    assert change_directory("/foo/", "/baz") == "/baz"
    assert change_directory("/", "foo/bar/../baz") == "/foo/baz"
    assert change_directory("/", "..") == "/"
    assert change_directory("/foo/bar", "baz", {"/foo/bar": "/abc"}) == "/abc/baz"
    assert (
        change_directory(
            "/foo/bar", "baz", {"/foo/bar": "/abc", "/abc": "/bcd", "/bcd/baz": "/xyz"}
        )
        == "/xyz"
    )
    assert (
        change_directory("/foo/bar", "baz", {"/foo/bar": "/abc", "/foo/bar/baz": "xyz"})
        == "/abc/baz"
    )
    assert (
        change_directory(
            "/foo/bar",
            "baz",
            {
                "/foo/bar": "/abc",
                "/foo/bar/baz": "xyz",
                "/abc": "/bcd",
                "/bcd/baz": "/xyz",
            },
        )
        == "/xyz"
    )
    assert (
        change_directory(
            "/foo/bar",
            "baz",
            {
                "/foo/bar": "/abc",
                "/foo/bar/baz": "xyz",
                "/abc": "/bcd",
                "/bcd/baz": "/xyz",
            },
        )
        == "/xyz"
    )
