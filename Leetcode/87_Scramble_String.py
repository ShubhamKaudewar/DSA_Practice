import pytest

class Solution:
    def isScramble(self, s1: str, s2: str) -> bool:
        return False

    # def randomSwap(self, s1, s2) -> bool:
    #     if len(s1) <= 1:
    #         return s1 == s2
    #     match = False
    #
    #
    #     def dfs(s):
    #         nonlocal match
    #         if len(s) == 1:
    #             return s
    #
    #         for i in range(1, len(s)):
    #             first = s[:1]
    #             second = s[1:]
    #
    #             left = dfs(first)
    #             right = dfs(second)
    #             if left+right == s2:
    #                 match = True
    #                 return None
    #
    #             left = dfs(second)
    #             right = dfs(first)
    #             if left+right == s2:
    #                 match = True
    #                 return None
    #
    #         return
    #
    #     dfs(s1)
    #     return match


def test_1():
    sol = Solution()
    s1 = "great"
    s2 = "rgeat"
    expected = True
    actual = sol.isScramble(s1, s2)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()