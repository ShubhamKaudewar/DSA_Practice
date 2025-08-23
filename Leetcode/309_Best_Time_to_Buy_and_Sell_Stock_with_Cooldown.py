import pytest
from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # We have two choice: buy/sell
        # buying: i+1
        # selling: i+2

        cache = {} # key: (i: int, buying: bool) value: (max_profit:int)
        def dfs(i, buying):
            if i >= len(prices): # last day we don't make any profit
                return 0

            if (i, buying) in cache:
                return cache[(i, buying)]

            cooldown = dfs(i + 1, buying) # cooldown is always option in case of both buy and sell, choice to hold for future
            if buying:
                buy = dfs(i+1, False) - prices[i] # If we are buying today means profit booked is selling onward profit - today price
                cache[(i, True)] = max(buy, cooldown)
            else:
                sell = prices[i] + dfs(i+2, True) # If we are selling today means profit booked is today's price + profit if we buy day after cool down
                cache[(i, False)] = max(sell, cooldown)
            return cache[(i, buying)]
        return dfs(0, True)


def test_case_1():
    sol = Solution()
    prices = [1,2,3,0,2]
    actual = sol.maxProfit(prices)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    prices = [1]
    actual = sol.maxProfit(prices)
    expected = 0
    assert actual == expected

if __name__ == '__main__':
    pytest.main()