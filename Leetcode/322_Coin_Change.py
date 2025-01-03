from typing import List

class Solution:
    def __init__(self):
        self.c = 0
        self.m = None

    def coinChange(self, coins: List[int], amount: int) -> int:
        if not amount:
            return 0
        self.m = [float('inf')] * (amount + 1)
        self.m[0] = 0  # Initialize base case

        coins.sort()

        for a in range(1, amount + 1):
            for c in coins:
                if c > a:
                    break
                self.m[a] = min(self.m[a], 1 + self.m[a - c])

        return self.m[amount] if self.m[amount] != float('inf') else -1

if __name__ == '__main__':
    sol = Solution()
    coins = [1, 2, 5]
    target = 11
    print(sol.coinChange(coins, target))