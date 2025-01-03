from typing import List
class Solution:
    def __init__(self):
        self.piles = None

    def eatTime(self, speed: int) -> int:
        time = 0
        for pile in self.piles:
            time += (pile + speed - 1) // speed  # This ensures we round up
        return time

    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        self.piles = piles
        left, right = 1, max(piles)

        while left < right:
            mid = (left + right) // 2
            if self.eatTime(mid) <= h:
                right = mid
            else:
                left = mid + 1
        return left

if __name__ == '__main__':
    sol = Solution()
    piles = [3,6,7,11]
    h = 8
    print(sol.minEatingSpeed(piles, h))
    piles = [30,11,23,4,20]
    h = 5
    print(sol.minEatingSpeed(piles, h))
    piles = [30,11,23,4,20]
    h = 6
    print(sol.minEatingSpeed(piles, h))