import unittest

from gpu_credit_tracker import GPUCreditTracker


class TestGPUCreditTracker(unittest.TestCase):
    def test_inserts_correctly(self):
        """Tests if the class inserts transactions correctly and gets the balance"""
        tracker = GPUCreditTracker()
        tracker.create_grant(10, 50, 5)
        tracker.create_grant(20, 60, 5)
        self.assertEqual(tracker.get_balance(19), 5)
        self.assertEqual(tracker.get_balance(20), 10)
        self.assertEqual(tracker.get_balance(50), 5)
        self.assertEqual(tracker.get_balance(60), 0)

    def test_subtracts_in_any_order_entered(self):
        """Tests if subtraction can be handled in any order that it's received"""
        tracker = GPUCreditTracker()
        tracker.create_grant(10, 50, 5)
        tracker.create_grant(20, 60, 5)
        self.assertEqual(tracker.get_balance(19), 5)
        tracker.subtract(15, 4)
        self.assertEqual(tracker.get_balance(10), 5)
        self.assertEqual(tracker.get_balance(20), 6)
        tracker.create_grant(15, 20, 8)
        self.assertEqual(tracker.get_balance(14), 5)
        self.assertEqual(tracker.get_balance(15), 9)
        self.assertEqual(tracker.get_balance(20), 10)

    def test_should_return_zero_for_no_grants(self):
        """Returns 0 for get_balance() if no grants have been created"""
        tracker = GPUCreditTracker()
        self.assertEqual(tracker.get_balance(10), 0)

    def test_handles_all_grants_expired(self):
        """Returns 0 if all grants have been expired"""
        tracker = GPUCreditTracker()
        tracker.create_grant(10, 50, 5)
        tracker.create_grant(20, 60, 5)
        self.assertEqual(tracker.get_balance(100), 0)


if __name__ == "__main__":
    unittest.main()
