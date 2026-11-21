from subtree_of_another_tree import TreeNode, isSubtree


def test_returns_true_if_subtree_found_in_main_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sub_root = TreeNode(2)
    sub_root.left = TreeNode(4)
    sub_root.right = TreeNode(5)
    assert isSubtree(root, sub_root)


def test_returns_false_if_subtree_not_found_in_main_tree():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    sub_root = TreeNode(2)
    sub_root.left = TreeNode(4)
    sub_root.right = TreeNode(6)
    assert not isSubtree(root, sub_root)


def test_returns_false_if_root_present_but_subtree_is_not():
    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)
    assert not isSubtree(root, None)


def test_returns_false_if_subtree_present_but_root_is_not():
    sub_root = TreeNode(1)
    sub_root.left = TreeNode(2)
    sub_root.right = TreeNode(3)
    assert not isSubtree(None, sub_root)


def test_returns_true_if_both_root_and_subtree_are_empty():
    assert isSubtree(None, None)
