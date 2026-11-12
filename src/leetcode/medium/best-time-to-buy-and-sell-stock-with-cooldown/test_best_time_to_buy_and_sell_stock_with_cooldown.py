from best_time_to_buy_and_sell_stock_with_cooldown import maxProfit


def test_returns_for_small_list():
    prices = [1, 2, 3, 0, 2]
    assert maxProfit(prices) == 3


def test_returns_zero_when_no_sell():
    prices = [1]
    assert maxProfit(prices) == 0
