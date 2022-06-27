from clone_graph import Node, clone_graph
import unittest

class TestCloneGraph(unittest.TestCase):
    def test_returns_empty_node_if_no_neighbors(self):
        """Takes in a root node with no neighbors and returns an empty list"""
        result = clone_graph(Node(1, []))
        self.assertEqual(result.val, 1)
        self.assertEqual(result.neighbors, [])

    def test_returns_full_cloned_list(self):
        """Takes in graph and clones it"""
        root = Node(1, [])
        second = Node(2, [])
        third = Node(3, [])
        fourth = Node(4, [])
        root.neighbors = [second, third]
        second.neighbors = [third, fourth]
        third.neighbors = [root, fourth]
        fourth.neighbors = [second, root]

        result = clone_graph(root)
        self.assertEqual(result.val, 1)
        self.assertEqual(len(result.neighbors), 2)
        self.assertEqual(root.neighbors[0].val, 2)
        self.assertEqual(len(root.neighbors[0].neighbors), 2)
        self.assertEqual(root.neighbors[1].val, 3)
        self.assertEqual(len(root.neighbors[1].neighbors), 2)

if __name__ == "__main__":
    unittest.main()