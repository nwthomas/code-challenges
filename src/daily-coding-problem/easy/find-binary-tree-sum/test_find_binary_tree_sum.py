from find_binary_tree_sum import Node, BinaryTree
import unittest


def create_root_bst(root_value):
    bst = BinaryTree()
    bst.add_value(root_value)
    return bst


def create_full_bst(num_list):
    bst = BinaryTree()

    for num in num_list:
        bst.add_value(num)

    return bst


class TestNode(unittest.TestCase):
    def test_instantiates(self):
        """Tests that the Node class can be instantiated with a given value"""
        node = Node(1)
        self.assertIsInstance(node, Node)
        self.assertEqual(node.value, 1)


class TestBinaryTree(unittest.TestCase):
    def test_instantiates(self):
        """Tests that the BinaryTree class can be instantiated"""
        bst = BinaryTree()
        self.assertIsInstance(bst, BinaryTree)

    def test_creates_root_node(self):
        """Tests that a root node will be created successfully with a given value"""
        bst = BinaryTree()
        bst.add_value(10)
        self.assertEqual(bst.root.value, 10)

    def test_adds_value_to_right(self):
        """Tests if a value can be added to the right of the tree"""
        bst = create_root_bst(10)
        bst.add_value(15)
        self.assertEqual(bst.root.right.value, 15)

    def test_adds_value_to_left(self):
        """Tests if a value can be added to the left of the tree"""
        bst = create_root_bst(10)
        bst.add_value(5)
        self.assertEqual(bst.root.left.value, 5)

    def test_returns_true_if_total_exists_in_tree(self):
        """Tests if a total can be found going from the root to a leaf"""
        bst = create_full_bst([7, 4, 10, 11, 10, 8, 7, 3, 2, 5, 3])
        result = bst.find_if_sum_exists(38)
        self.assertTrue(result)

    def test_returns_false_if_total_does_not_exist_in_tree(self):
        """Tests if a total cannot be found going from the root to a leaf"""
        bst = create_full_bst([7, 4, 10, 11, 10, 8, 7, 3, 2, 5, 3])
        result = bst.find_if_sum_exists(100)
        self.assertFalse(result)


if __name__ == "__main__":
    unittest.main()
