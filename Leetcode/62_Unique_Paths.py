import pytest
import importlib
pascalsTriangle = importlib.import_module("118_Pascal's_Triangle")

class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        result = pascalsTriangle.Solution().generate(m+n-1)
        return result[n+1][-m]

def test_case_1():
    sol = Solution()
    m = 3
    n = 7
    expected = 28
    actual = sol.uniquePaths(m, n)
    assert actual == expected

def test_case_2():
    sol = Solution()
    m = 3
    n = 2
    expected = 3
    actual = sol.uniquePaths(m, n)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()