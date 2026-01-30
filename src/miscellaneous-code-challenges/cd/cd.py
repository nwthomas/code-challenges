"""
Implement a function cd(current_dir, new_dir) that returns the resulting path.

Examples:
cd(/foo/bar, baz) = /foo/bar/baz
cd(/foo/../, ./baz) = /baz
cd(/, foo/bar/../baz) = /baz
cd(/, ..) = Null

Part 2: Add support for the ~ symbol (home directory).
Difficulty upgrade (Part 3): Add a third parameter soft_link (a dictionary of symbolic links).

Examples:
cd(/foo/bar, baz, {/foo/bar: /abc}) = /abc/baz
cd(/foo/bar, baz, {/foo/bar: /abc, /abc: /bcd, /bcd/baz: /xyz}) = /xyz

The soft link dictionary may contain both short and long matches; the longer/more specific path should take precedence.

Example:
cd(/foo/bar, baz, {/foo/bar: /abc, /foo/bar/baz: xyz}) = xyz

Detect cycles in the soft link dictionary (e.g., A→B, B→A).
"""


def get_symlinked_path(current_path: str, symlinks: dict[str, str]) -> str:
    visited = set[str]()

    current = current_path
    while current in symlinks:
        if current in visited:
            return current_path
        visited.add(current)
        current = symlinks[current]

    return current


def change_directory(
    current_path: str, new_path: str, symlinks: dict[str, str] = None
) -> str:
    if symlinks is None:
        symlinks = {}

    current_path = get_symlinked_path(current_path, symlinks)
    stack = [s for s in current_path.split("/") if s != ""]

    if len(new_path) > 0 and new_path[0] == "/":
        stack = []

    paths = [s for s in new_path.split("/") if s != "" and s != "."]
    for path in paths:
        if path == ".." and len(stack) > 0:
            stack.pop()
        elif path != "..":
            stack.append(path)
        stack = [
            s
            for s in get_symlinked_path("/" + "/".join(stack), symlinks).split("/")
            if s != "" and s != "."
        ]

    return "/" + "/".join(stack)
