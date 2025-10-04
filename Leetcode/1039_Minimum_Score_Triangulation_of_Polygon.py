import pytest
from typing import List

class Solution:
    def minScoreTriangulation(self, values: List[int]) -> int:


def test_case_1():
    sol = Solution()
    values = [1,2,3]
    actual = sol.minScoreTriangulation(values)
    expected = 6
    assert actual == expected

def test_case_2():
    sol = Solution()
    values = [3,7,4,5]
    actual = sol.minScoreTriangulation(values)
    expected = 144
    assert actual == expected

if __name__ == '__main__':
    pytest.main()