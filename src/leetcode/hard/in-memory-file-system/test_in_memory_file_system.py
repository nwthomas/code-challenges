from in_memory_file_system import FileSystem
import unittest

# TODO: Finish and debug draft code in in_memory_file_system

class TestFileSystem(unittest.TestCase):
    def test_creates_file_system(self):
        """Instantiates a new FileSystem"""
        fs = FileSystem()
        self.assertIsInstance(fs, FileSystem)

    def test_adds_new_dir_with_mkdir(self):
        """Creates new directory using mkdir method"""
        fs = FileSystem()
        fs.mkdir("/a")
        result = fs.ls("/")
        self.assertEqual(result, ["a"])

    def test_adds_deeply_nested_directory(self):
        """Creates deeply nested directory using mkdir method"""
        fs = FileSystem()
        fs.mkdir("/a/b/c/d")
        result = fs.ls("/a/b/c")
        self.assertEqual(result, ["d"])

        fs.mkdir("/a/b/c/e")
        fs.mkdir("/a/b/c/f")

        result = fs.ls("/a/b/c")
        self.assertEqual(result, ["d", "e", "f"])

    def test_can_ls_different_paths(self):
        """Creates different file paths and can ls between them"""
        fs = FileSystem()
        fs.mkdir("/a/b/c/d/e/f/g")
        fs.mkdir("/a/b/c/r/t/y")
        fs.mkdir("/a/b/c/r/d")
        fs.mkdir("/a/b/c/d/e/h")

        result = fs.ls("/a/b/c/d/e")
        self.assertEqual(result, ["f", "h"])

        result = fs.ls("/a/b/c/r/t")
        self.assertEqual(result, ["y"])

    def test_can_add_new_file_with_contents(self):
        """Creates a new file with new content"""
        fs = FileSystem()
        fs.mkdir("/test/another/test")
        fs.addContentToFile("/test/another/test/haha", "this is test content")
        
        result = fs.readContentFromFile("/test/another/test/haha")
        self.assertEqual(result, "this is test content")

    def test_can_add_content_to_existing_file(self):
        """Adds new file content to an existing file"""
        fs = FileSystem()
        fs.mkdir("/test/another/test")
        fs.addContentToFile("/test/another/test/haha", "this is test content")

        fs.addContentToFile("/test/another/test/haha", " additional content")

        result = fs.readContentFromFile("/test/another/test/haha")
        self.assertEqual(result, "this is test content additional content")

    def test_can_create_dirs_while_creating_file(self):
        """Can create directories while creating a new file"""
        fs = FileSystem()
        fs.addContentToFile("/a/b/c/d/final", "did this work?")

        result = fs.readContentFromFile("/a/b/c/d/final")
        self.assertEqual(result, "did this work?")

if __name__ == "__main__":
    unittest.main()