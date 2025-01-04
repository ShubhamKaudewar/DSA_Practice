from typing import List
import pytest


class StockSpanner:
    def __init__(self):
        self.spanner = []

    def next(self, price: int) -> int:
        curr_trend = 1
        while self.spanner and self.spanner[-1][0] <= price:
            curr_trend += self.spanner.pop()[1]

        self.spanner.append((price, curr_trend))
        return curr_trend

def test_case_1():
    actions = ["StockSpanner", "next", "next", "next", "next", "next", "next", "next"]
    prices = [[], [100], [80], [60], [70], [60], [75], [85]]
    result, sp = [], None
    for action, price in zip(actions, prices):
        if action == "StockSpanner":
            sp = StockSpanner()
            result.append(None)
        else:
            result.append(sp.next(*price))
    assert result == [None, 1, 1, 1, 2, 1, 4, 6]

if __name__ == '__main__':
    pytest.main()