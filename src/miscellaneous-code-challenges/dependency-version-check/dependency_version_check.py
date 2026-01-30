"""
You are given a list of dependency versions, e.g., [103.003.02, 103.003.03, 203.003.02].

Each version may support or not support a specific feature.

Task: Find the earliest version that supports the current feature.
"""

from typing import Callable


def parse(version: str) -> tuple[str]:
    return tuple[str](int(val) for val in version.split("."))


def find_earliest_supported_version(
    versions: tuple[str], is_supported: Callable[str]
) -> str | None:
    parsed = [parse(version) for version in versions]
    sorted_versions = sorted(parsed)

    l = 0
    r = len(sorted_versions) - 1
    earliest_version = None

    while l <= r:
        pivot = (l + r) // 2

        version = sorted_versions[pivot]
        joined_version = ".".join([str(v) for v in version])

        if is_supported(joined_version):
            earliest_version = joined_version
            r = pivot - 1
        else:
            l = pivot + 1

    if not earliest_version:
        return None

    return earliest_version
