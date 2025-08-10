import pytest

class Solution:
    """
    This is question of 2D DP, can be solved using 2D table and bottom-up approach (dfs)
    We will be using memoization by creating 2D array called cache and storing values there
    """
    def longestCommonSubsequence(self, text1: str, text2: str) -> int:
        row = len(text1)
        col = len(text2)
        cache = [[0] * (col + 1) for _ in range(row + 1)]

        for i in range(row - 1, -1, -1):
            for j in range(col - 1, -1, -1):
                if text1[i] == text2[j]:
                    cache[i][j] = 1 + cache[i + 1][j + 1] # We will be taking value of next diagonal index
                else:
                    cache[i][j] = max(cache[i + 1][j], cache[i][j + 1]) # We will take adjacent max value

        return cache[0][0]


def test_case_1():
    sol = Solution()
    text1 = "abcde"
    text2 = "ace"
    expected = 3
    actual = sol.longestCommonSubsequence(text1, text2)
    assert actual == expected

def test_case_2():
    sol = Solution()
    text1 = "abc"
    text2 = "abc"
    expected = 3
    actual = sol.longestCommonSubsequence(text1, text2)
    assert actual == expected

def test_case_3():
    sol = Solution()
    text1 = "abc"
    text2 = "def"
    expected = 0
    actual = sol.longestCommonSubsequence(text1, text2)
    assert actual == expected

def test_case_4():
    sol = Solution()
    text1 = "cat"
    text2 = "crabt"
    expected = 3
    actual = sol.longestCommonSubsequence(text1, text2)
    assert actual == expected



if __name__ == '__main__':
    pytest.main()