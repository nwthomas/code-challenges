from gpu_credit_tracker import GPUCreditTracker


def test_inserts_correctly():
    """Tests if the class inserts transactions correctly and gets the balance"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    credit.create_grant(20, 60, 5)
    assert credit.get_balance(19) == 5
    assert credit.get_balance(20) == 10
    assert credit.get_balance(50) == 5
    assert credit.get_balance(60) == 0


def test_subtracts_from_expiring_grants_first():
    """Tests if subtraction can be handled from expiring grants first"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    credit.create_grant(14, 60, 10)
    assert credit.get_balance(15) == 15
    credit.subtract(15, 10)
    assert credit.get_balance(10) == 5
    assert credit.get_balance(14) == 15
    assert credit.get_balance(15) == 5
    assert credit.get_balance(59) == 5
    assert credit.get_balance(60) == 0


def test_subtracts_in_any_order_entered():
    """Tests if subtraction can be handled in any order that it's received"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    credit.create_grant(20, 60, 5)
    assert credit.get_balance(19) == 5
    credit.subtract(15, 4)
    assert credit.get_balance(10) == 5
    assert credit.get_balance(20) == 6
    credit.create_grant(14, 20, 8)
    assert credit.get_balance(14) == 13
    assert credit.get_balance(15) == 9
    assert credit.get_balance(20) == 10


def test_should_return_zero_for_no_grants():
    """Returns 0 for get_balance() if no grants have been created"""
    credit = GPUCreditTracker()
    assert credit.get_balance(10) == 0
    assert credit.get_balance(100000000) == 0


def test_handles_all_grants_expired():
    """Returns 0 if all grants have been expired"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    credit.create_grant(20, 60, 5)
    assert credit.get_balance(100) == 0


def test_handles_negative_balance():
    """Returns None if the balance goes negative"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    credit.subtract(15, 6)
    credit.create_grant(16, 20, 8)
    assert credit.get_balance(15) == None
    assert credit.get_balance(16) == None
    assert credit.get_balance(20) == None
    assert credit.get_balance(100000000) == None
    credit.create_grant(11, 100, 10)
    assert credit.get_balance(10) == 5
    assert credit.get_balance(11) == 15
    assert credit.get_balance(15) == 9
    assert credit.get_balance(16) == 17
    assert credit.get_balance(20) == 9


def test_balance_before_first_transaction():
    """Returns 0 for get_balance(ts) when ts is before the first transaction"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    assert credit.get_balance(5) == 0
    assert credit.get_balance(9) == 0


def test_exact_expiration_boundary():
    """Grant is not counted at the expiration instant (expiration is exclusive)"""
    credit = GPUCreditTracker()
    credit.create_grant(10, 50, 5)
    assert credit.get_balance(49) == 5
    assert credit.get_balance(50) == 0


def test_insert_transaction_places_earlier_transaction_at_start():
    """Transaction with timestamp before all existing ones is inserted at start, not end."""
    credit = GPUCreditTracker()
    credit.create_grant(20, 60, 5)
    credit.create_grant(10, 50, 3)
    assert credit.get_balance(15) == 3
    assert credit.get_balance(25) == 8
