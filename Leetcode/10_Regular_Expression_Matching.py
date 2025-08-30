import re
import pytest
from typing import List
from functools import lru_cache

class Solution:
    def isMatch(self, s: str, p: str) -> bool:
        @lru_cache(maxsize=None)
        def dfs(i, j):
            if j == len(p):
                return i == len(s)

            first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                return dfs(i, j+2) or first_match and dfs(i+1, j)
                """Above can be written as
                # using wildcard
                ans1 = first_match and dfs(i+1, j) 

                # skipping wildcard
                ans2 = dfs(i, j+2)
                return ans1 or ans2
                """

            else:
                return first_match and dfs(i+1, j+1) # move diagonally
        return dfs(0, 0)

    def isMatch2(self, s: str, p: str) -> bool:

        dp = [[None] * (len(p)+1) for _ in range(len(s)+1)] # visited

        def dfs(i, j):
            if dp[i][j] is not None:
                return dp[i][j]

            if j == len(p):
                dp[i][j] = i == len(s)
                return dp[i][j]

            first_match = i < len(s) and (s[i] == p[j] or p[j] == ".")
            if j+1 < len(p) and p[j+1] == "*":
                # using wildcard
                ans1 = first_match and dfs(i+1, j)

                # skipping wildcard
                ans2 = dfs(i, j+2)
                dp[i][j] = ans1 or ans2
            else:
                dp[i][j] = first_match and dfs(i+1, j+1) # move diagonally

            return dp[i][j]
        return dfs(0, 0)

    def isMatch1(self, s: str, p: str) -> bool:
        """This is also one solution"""

        pattern = re.compile(fr"{p}")
        match = pattern.fullmatch(s)
        if match:
            return True
        return False


def test_case_1():
    sol = Solution()
    s = "aa"
    p = "a"
    expected = False
    actual = sol.isMatch(s, p)
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "aa"
    p = "a*"
    expected = True
    actual = sol.isMatch(s, p)
    assert actual == expected
#
def test_case_3():
    sol = Solution()
    s = "ab"
    p = ".*"
    expected = True
    actual = sol.isMatch(s, p)
    assert actual == expected


def test_case_4():
    sol = Solution()
    s = "aab"
    p = "c*a*b"
    expected = True
    actual = sol.isMatch(s, p)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()