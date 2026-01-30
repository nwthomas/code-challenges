from dependency_version_check import find_earliest_supported_version


def test_is_supported_earliest_version():
    def is_supported(version: str) -> bool:
        supported_versions = {
            "1.1.3",
            "3.11.2",
            "3.12.4",
            "4.5.0",
            "4.5.1",
            "4.60.200",
            "12.0.1",
            "101.567.1",
        }
        return version in supported_versions

    versions = {
        "1.0.1",
        "1.1.2",
        "1.1.3",
        "3.11.2",
        "3.11.3",
        "3.12.4",
        "4.5.0",
        "4.5.1",
        "4.60.200",
        "12.0.1",
        "101.567.1",
    }

    assert find_earliest_supported_version(versions, is_supported) == "1.1.3"


def test_is_not_supported_earliest_version():
    def is_supported(version: str) -> bool:
        supported_versions = {}

    versions = {
        "1.0.1",
        "1.1.2",
        "1.1.3",
        "3.11.2",
        "3.11.3",
        "3.12.4",
        "4.5.0",
        "4.5.1",
        "4.60.200",
        "12.0.1",
        "101.567.1",
    }

    assert find_earliest_supported_version(versions, is_supported) is None
