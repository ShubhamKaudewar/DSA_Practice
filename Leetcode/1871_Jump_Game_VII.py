import pytest
from functools import lru_cache

class Solution:
    def canReach(self, s: str, minJump: int, maxJump: int) -> bool:
        n = len(s)
        dp = [False] * n
        dp[0] = True
        reachable = 0  # sliding window count

        for i in range(1, n):
            if i - minJump >= 0 and dp[i - minJump]:
                reachable += 1
            if i - maxJump - 1 >= 0 and dp[i - maxJump - 1]:
                reachable -= 1

            # mark reachable if window has at least one True and s[i] == '0'
            dp[i] = (s[i] == '0' and reachable > 0)

        return dp[-1]


    def canReach1(self, s: str, minJump: int, maxJump: int) -> bool:
        """This is good but this is not sufficient for TLE"""
        n = len(s)

        @lru_cache(None)
        def bfs(i):
            if i == n-1:
                return True

            for j in range(i + minJump, min(i+maxJump, n-1) + 1):
                if s[j] == "0" and bfs(j):
                    return True
            return False

        return bfs(0)


def test_case_1():
    sol = Solution()
    s = "011010"
    minJump = 2
    maxJump = 3
    actual = sol.canReach(s, minJump, maxJump)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "01101110"
    minJump = 2
    maxJump = 3
    actual = sol.canReach(s, minJump, maxJump)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()