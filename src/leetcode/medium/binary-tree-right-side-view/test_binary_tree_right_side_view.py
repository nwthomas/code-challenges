from collections import deque
from typing import Optional

from binary_tree_right_side_view import TreeNode, rightSideView


def build_tree(values: list[Optional[int]]) -> Optional[TreeNode]:
    if not values or values[0] is None:
        return None

    root = TreeNode(values[0])
    queue = deque([root])
    i = 1

    while queue and i < len(values):
        node = queue.popleft()

        if i < len(values) and values[i] is not None:
            node.left = TreeNode(values[i])
            queue.append(node.left)
        i += 1

        if i < len(values) and values[i] is not None:
            node.right = TreeNode(values[i])
            queue.append(node.right)
        i += 1

    return root


def test_returns_none_for_empty_tree():
    root = None
    assert not rightSideView(root)


def test_returns_right_side_view():
    root = build_tree([1, 2, 3, None, 5, None, 4])
    assert rightSideView(root) == [1, 3, 4]


def test_returns_longer_right_side_view():
    root = build_tree([1, 2, 3, 4, None, None, None, 5])
    assert rightSideView(root) == [1, 3, 4, 5]
