from in_memory_file_system import FileSystem
import unittest

# TODO: Finish and debug draft code in in_memory_file_system

class TestFileSystem(unittest.TestCase):
    def test_creates_file_system(self):
        result = FileSystem()
        print(result._getFilePathList("/d/g/a/d/a"))

if __name__ == "__main__":
    unittest.main()