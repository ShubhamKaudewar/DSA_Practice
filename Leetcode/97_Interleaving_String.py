from typing import List
import pytest


class Solution:
    """This is question of dfs check knapsack by either taking char from string s1 or string s2
    Below code is more polished version of second part"""
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        if len(s3) != len(s1) + len(s2):
            return False

        cache = {}

        def dfs(i, j, k):
            if (i, j, k) in cache:
                return cache[(i, j, k)]

            if k == len(s3):
                return True

            match_s1 = i < len(s1) and s1[i] == s3[k] and dfs(i + 1, j, k + 1)
            match_s2 = j < len(s2) and s2[j] == s3[k] and dfs(i, j + 1, k + 1)

            cache[(i, j, k)] = match_s1 or match_s2
            return cache[(i, j, k)]

        return dfs(0, 0, 0)

    def isInterleave2(self, s1: str, s2: str, s3: str) -> bool:
        cache = {}
        if len(s3) < len(s1) + len(s2):
            return False

        def dfs(l, r, p):
            if (l, r, p) in cache:
                return cache[(l, r, p)]

            if p == len(s3):
                cache[(l, r, p)] = True
                return True


            if l >= len(s1) and r >= len(s2):
                return False

            if l < len(s1) and s3[p] != s1[l]:
                if r < len(s2) and s3[p] != s2[r]:
                    return False

            # To include left char
            is_left, is_right = False, False
            if l < len(s1) and s3[p] == s1[l]:
                is_left = dfs(l+1, r, p+1)
            cache[(l+1, r, p+1)] = is_left

            if r < len(s2) and s3[p] == s2[r]:
                is_right = dfs(l, r+1, p+1)
            cache[(l+1, r, p+1)] = is_right

            return is_left or is_right

        return dfs(0, 0, 0)


def test_case_1():
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbcbcac"
    actual = sol.isInterleave(s1, s2, s3)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    s1 = "aabcc"
    s2 = "dbbca"
    s3 = "aadbbbaccc"
    actual = sol.isInterleave(s1, s2, s3)
    expected = False
    assert actual == expected

def test_case_3():
    sol = Solution()
    s1 = "aabc"
    s2 = "abad"
    s3 = "aabadabc"
    actual = sol.isInterleave(s1, s2, s3)
    expected = True
    assert actual == expected

def test_case_4():
    sol = Solution()
    s1 = "a"
    s2 = "b"
    s3 = "a"
    actual = sol.isInterleave(s1, s2, s3)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()