import importlib

import pytest

Solution = importlib.import_module(
    "top_interview_150.2_best_time_to_buy_and_sell_stock"
).Solution


def max_profit(prices: list[int]) -> int:
    return Solution().maxProfit(prices)


def test_example1():
    assert max_profit([7, 1, 5, 3, 6, 4]) == 7


def test_example2():
    assert max_profit([1, 2, 3, 4, 5]) == 4


def test_example3():
    assert max_profit([7, 6, 4, 3, 1]) == 0


def test_single_element():
    assert max_profit([5]) == 0


def test_two_elements_profit():
    assert max_profit([1, 5]) == 4


def test_two_elements_no_profit():
    assert max_profit([5, 1]) == 0


def test_alternating():
    assert max_profit([1, 3, 1, 3, 1]) == 4


def test_all_same():
    assert max_profit([3, 3, 3]) == 0
