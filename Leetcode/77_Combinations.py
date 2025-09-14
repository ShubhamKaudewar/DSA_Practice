from copy import deepcopy
from typing import List
import pytest

class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        """Instead of maintaining level to match K we can check against len of parent and create a shallow copy"""
        result = []

        def dfs(start, parent):
            if len(parent) == k:
                result.append(parent[:])
                return

            for i in range(start, n+1):
                parent.append(i)
                dfs(i+1, parent)
                parent.pop(-1)

        dfs(1, [])
        return result

    def combine1(self, n: int, k: int) -> List[List[int]]:
        result = []

        def dfs(start, lvl, parent):
            if lvl > k:
                result.append(deepcopy(parent))
                return

            for i in range(start, n+1):
                parent.append(i)
                dfs(i+1, lvl+1, parent)
                parent.pop(-1)

        dfs(1, 1, [])
        return result




def test_case_1():
    sol = Solution()
    n = 4
    k = 2
    actual = sol.combine(n, k)
    expected = [[1,2],[1,3],[1,4],[2,3],[2,4],[3,4]]
    assert actual == expected

def test_case_2():
    sol = Solution()
    n = 1
    k = 1
    actual = sol.combine(n, k)
    expected = [[1]]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()