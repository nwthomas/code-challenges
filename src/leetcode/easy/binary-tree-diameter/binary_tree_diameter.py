
from typing import Optional


class TreeNode:
    def __init__(self, val: int = 0, left: Optional["TreeNode"] = None, right: Optional["TreeNode"] = None):
        self.val = val
        self.left = left
        self.right = right


def diameterOfBinaryTree(root: Optional[TreeNode]) -> int:
    def bfs(node: Optional[TreeNode]) -> dict[str, int]:
        if not node:
            return {"longestDiameter": 0, "longestCurrent": 0}

        left = bfs(node.left)
        right = bfs(node.right)

        longestCurrent = left["longestCurrent"]
        if left["longestCurrent"] < right["longestCurrent"]:
            longestCurrent = right["longestCurrent"]
        longestCurrent += 1

        longestDiameter = right["longestCurrent"] + left["longestCurrent"]
        if left["longestDiameter"] > longestDiameter:
            longestDiameter = left["longestDiameter"]
        if right["longestDiameter"] > longestDiameter:
            longestDiameter = right["longestDiameter"]

        return {"longestDiameter": longestDiameter, "longestCurrent": longestCurrent}

    result = bfs(root)

    return result["longestDiameter"]
