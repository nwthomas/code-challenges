from deep_clone_random_pointer_list import deep_clone_random_pointer_list, Node
import unittest

class TestDeepCloneRandomPointerList(unittest.TestCase):
    def is_same_list(self, l1, l2):
        stack = [[l1, l2]]
        cache = {}

        while len(stack) > 0:
            current_l1, current_l2 = stack.pop()

            if current_l1 == current_l2:
                return False
            if current_l1.value != current_l2.value:
                return False
            if (current_l1.next_node and not current_l2.next_node) or (current_l2.next_node and not current_l1.next_node):
                return False
            if (current_l1.random_node and not current_l2.random_node) or (current_l2.random_node and not current_l1.random_node):
                return False

            cache[current_l1] = True
            cache[current_l2] = True

            if current_l1.next_node and not current_l1.next_node in cache:
                stack.append([current_l1.next_node, current_l2.next_node])
            if current_l1.random_node and not current_l2.random_node in cache:
                stack.append([current_l1.random_node, current_l2.random_node])

        return True

    def test_deep_clones_list(self):
        """Can deep clone a short list"""
        root = Node(1)
        root.next_node = Node(2)
        root.next_node.next_node = Node(3)
        root.next_node.next_node.next_node = Node(4)
        root.random_node = root.next_node.next_node
        root.next_node.random_node = root
        root.next_node.next_node.random_node = root.next_node

        result = deep_clone_random_pointer_list(root)
        self.assertTrue(self.is_same_list(root, result))

if __name__ == "__main__":
    unittest.main()