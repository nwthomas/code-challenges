from min_stack import MinStack
import unittest


class TestMinStack(unittest.TestCase):
    def test_returns_null_for_empty_stack(self):
        """Tests that the stack returns null for empty stack"""
        min_stack = MinStack()
        result = min_stack.push(1)
        self.assertEqual(result, None)

    def test_returns_null_for_pop(self):
        """Tests that the stack returns null for pop"""
        min_stack = MinStack()
        min_stack.push(1)
        result = min_stack.pop()
        self.assertEqual(result, None)


if __name__ == "__main__":
    unittest.main()