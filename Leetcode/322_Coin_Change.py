from typing import List
import pytest

class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        cache = [float('inf')] * (amount + 1)
        cache[0] = 0  # Initialize base case

        coins.sort()

        for a in range(1, amount + 1):
            for c in coins:
                if c > a:
                    break
                cache[a] = min(cache[a], 1 + cache[a - c])

        return cache[amount] if cache[amount] != float('inf') else -1


def test_case_1():
    sol = Solution()
    coins = [1, 2, 5]
    amount = 11
    actual = sol.coinChange(coins, amount)
    expected = 3
    assert actual == expected

if __name__ == '__main__':
    pytest.main()