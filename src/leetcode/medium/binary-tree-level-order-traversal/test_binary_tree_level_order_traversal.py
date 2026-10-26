from binary_tree_level_order_traversal import TreeNode, levelOrder


def test_traverses_tree_in_breadth_first_order():
    t = TreeNode(10)
    t.right = TreeNode(15)
    t.right.left = TreeNode(14)
    t.right.right = TreeNode(20)
    t.left = TreeNode(5)
    t.left.left = TreeNode(1)
    t.left.right = TreeNode(9)

    result = levelOrder(t)
    assert result == [[10], [5, 15], [1, 9, 14, 20]]
