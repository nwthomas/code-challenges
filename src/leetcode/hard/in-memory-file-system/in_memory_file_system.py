"""
https://leetcode.com/problems/design-in-memory-file-system/solution/

Design an in-memory file system to simulate the following functions:

ls: Given a path in string format. If it is a file path, return a list that only contains this file's name. If it is a directory path, return the list of file and directory names in this directory. Your output (file and directory names together) should in lexicographic order.

mkdir: Given a directory path that does not exist, you should make a new directory according to the path. If the middle directories in the path don't exist either, you should create them as well. This function has void return type.

addContentToFile: Given a file path and file content in string format. If the file doesn't exist, you need to create that file containing given content. If the file already exists, you need to append given content to original content. This function has void return type.

readContentFromFile: Given a file path, return its content in string format.

Example:
Input: 
["FileSystem","ls","mkdir","addContentToFile","ls","readContentFromFile"]
[[],["/"],["/a/b/c"],["/a/b/c/d","hello"],["/"],["/a/b/c/d"]]

Output:
[null,[],null,null,["a"],"hello"]

Note:
- You can assume all file or directory paths are absolute paths which begin with / and do not end with / except that the path is just "/".
- You can assume that all operations will be passed valid parameters and users will not attempt to retrieve file content or list a directory or file that does not exist.
- You can assume that all directory names and file names only contain lower-case letters, and same names won’t exist in the same directory.
"""

import typing

DirDict = typing.Dict[str, 'Dir']

class Dir:
    def __init__(self, isFile: bool = False, contents: str = "", name: str = ""):
        """Instantiates a new Dir (which can be a file or directory)"""
        self.name = name
        self.isFile = isFile
        self.contents = contents
        self.dirs = {}
        self.files = {}

    def getDirs(self) -> DirDict:
        """Returns all sub-directories"""
        return self.dirs

    def setDir(self, key: str) -> None:
        """Sets a sub-directory"""
        self.dirs[key] = Dir(False, "", key)
    
    def getFiles(self) -> DirDict:
        """Gets all files in the directory"""
        return self.files

    def setFile(self, key: str, contents: str = "") -> None:
        """Sets a file in the directory"""
        self.files[key] = Dir(True, contents, key)

    def addContents(self, contents: str) -> None:
        """Appends contents to a file"""
        if self.isFile:
            self.contents += contents

    def ls(self) -> typing.List[str]:
        lsValues = [k for k in self.getFiles().keys()] + [k for k in self.getDirs().keys()]
        lsValues.sort()

        return lsValues

    def __str__(self) -> str:
        """Returns the name of the class"""
        return self.name


class FileSystem:
    root: DirDict = None

    def __init__(self):
        self.root = Dir(False, "", "/")

    def ls(self, filePath: str) -> typing.List[str]:
        filePathList = self._getFilePathList(filePath)
        filePathList.reverse()
        current = self.root

        if len(filePathList) == 0:
            return current.ls()

        while len(filePathList) > 0:
            currentPath = filePathList.pop()
            current = current.getDirs()[currentPath]

        return current.ls()
            
    def mkdir(self, filePath: str) -> None:
        filePathList = self._getFilePathList(filePath)
        filePathList.reverse()

        current = self.root

        while len(filePathList):
            currentPath = filePathList.pop()
            current = self._getDirAndCreateIfNeeded(current, currentPath)

    def addContentToFile(self, filePath: str, contents: str) -> None:
        filePathList = self._getFilePathList(filePath)
        fileName = filePathList.pop()

        filePathList.reverse()

        current = self.root

        while len(filePathList):
            currentPath = filePathList.pop()
            current = self._getDirAndCreateIfNeeded(current, currentPath)

        if fileName in current.files:
            current.files[fileName].addContents(contents)
        else:
            current.files[fileName] = Dir(True, contents, fileName)

    def readContentFromFile(self, filePath: str) -> str:
        filePathList = self._getFilePathList(filePath)
        fileName = filePathList.pop()

        filePathList.reverse()

        current = self.root

        while len(filePathList) > 0:
            currentPath = filePathList.pop()
            current = current.getDirs()[currentPath]

        return current.getFiles()[fileName].contents

    def _getFilePathList(self, filePath: str) -> typing.List[str]:
        if filePath == "/":
            return []

        filePath = filePath.split("/")
        
        return filePath[1:]

    def _getDirAndCreateIfNeeded(self, dir: Dir, currentPath: str) -> Dir:
        if not currentPath in dir.dirs:
            dir.dirs[currentPath] = Dir(False, "", currentPath)

        return dir.dirs[currentPath]

