from binary_tree_diameter import TreeNode, diameterOfBinaryTree


def test_handles_empty_tree():
    """Handles a root node of None for diameter of 0"""
    t = None
    result = diameterOfBinaryTree(t)
    assert result == 0


def test_handles_few_node_in_tree():
    """Handles a small tree and returns correct diameter"""
    left = TreeNode(1)
    right = TreeNode(2)
    t = TreeNode(2, left, right)
    result = diameterOfBinaryTree(t)
    assert result == 2


def test_handles_lopsided_tree():
    """Handles a lopsided tree (even if incorrect BST)"""
    leftOne = TreeNode(1)
    leftTwo = TreeNode(2, leftOne)
    leftThree = TreeNode(3, leftTwo)
    t = TreeNode(4, leftThree)
    result = diameterOfBinaryTree(t)
    assert result == 3


def test_handles_large_balanced_bst():
    """Handles a large balanced BST"""

    # Level 4
    n1 = TreeNode(1)
    n3 = TreeNode(3)
    n5 = TreeNode(5)
    n7 = TreeNode(7)
    n9 = TreeNode(9)
    n11 = TreeNode(11)
    n13 = TreeNode(13)
    n15 = TreeNode(15)

    # Level 3
    n2 = TreeNode(2, n1, n3)
    n6 = TreeNode(6, n5, n7)
    n10 = TreeNode(10, n9, n11)
    n14 = TreeNode(14, n13, n15)

    # Level 2
    n4 = TreeNode(4, n2, n6)
    n12 = TreeNode(12, n10, n14)

    # Root
    t = TreeNode(8, n4, n12)

    result = diameterOfBinaryTree(t)

    assert result == 6
