from min_stack import MinStack
import unittest


class TestMinStack(unittest.TestCase):
    def test_returns_inf_for_min_on_empty_stack(self):
        """Tests that the stack returns inf for min on empty stack"""
        min_stack = MinStack()
        result = min_stack.getMin()
        self.assertEqual(result, float('inf'))
    
    def test_returns_inf_for_top_on_empty_stack(self):
        """Tests that the stack returns inf for top on empty stack"""
        min_stack = MinStack()
        result = min_stack.top()
        self.assertEqual(result, float('inf'))
    
    def test_returns_correct_min_after_variety_of_numbers_pushed_to_it(self):
        """Tests that the stack returns correct min after variety of numbers pushed to it"""
        min_stack = MinStack()
        min_stack.push(1)
        min_stack.push(2)
        min_stack.push(0)
        min_stack.pop()
        min_stack.push(-10)
        min_stack.push(10)
        min_stack.pop()
        result = min_stack.getMin()
        self.assertEqual(result, -10)
    
    def test_returns_correct_top_after_variety_of_numbers_pushed_to_it(self):
        """Tests that the stack returns correct top after variety of numbers pushed to it"""
        min_stack = MinStack()
        min_stack.push(1)
        min_stack.push(2)
        min_stack.push(0)
        min_stack.push(-100)
        min_stack.pop()
        min_stack.push(-5)
        min_stack.push(100)
        min_stack.pop()
        result = min_stack.top()
        self.assertEqual(result, -5)

if __name__ == "__main__":
    unittest.main()