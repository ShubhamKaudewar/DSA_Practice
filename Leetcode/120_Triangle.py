from typing import List
import pytest
from functools import cache

class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        depth = len(triangle)

        @cache
        def dfs(idx, lvl):
            if lvl == depth:
                return 0

            # take idx=i
            curr = triangle[lvl][idx]
            return curr + min(dfs(idx, lvl + 1), dfs(idx + 1, lvl + 1))

        return dfs(0, 0)


    def minimumTotal1(self, triangle: List[List[int]]) -> int:
        """This same but use memo as cache"""
        depth = len(triangle)
        memo = {}

        def dfs(idx, lvl):
            if lvl == depth:
                return 0

            if (idx, lvl) in memo:
                return memo[(idx, lvl)]
            curr = triangle[lvl][idx]
            memo[(idx, lvl)] = curr + min(dfs(idx, lvl + 1), dfs(idx + 1, lvl + 1))
            return memo[(idx, lvl)]

        return dfs(0, 0)

    def minimumTotal2(self, triangle: List[List[int]]) -> int:
        """This is giving TLE, not using cache/memoization"""
        depth = len(triangle)

        def dfs(idx, lvl, path):
            if lvl == depth:
                return path

            # take idx=i
            path += triangle[lvl][idx]
            path1 = dfs(idx, lvl+1, path)
            path -= triangle[lvl][idx]

            # take idx=i+1
            if idx < len(triangle[lvl])-1:
                path += triangle[lvl][idx+1]
                path2 = dfs(idx+1, lvl+1, path)
                return min(path1, path2)
            return path1

        ans = dfs(0, 0, 0)
        return ans


def test_case_1():
    sol = Solution()
    triangle = [[2],[3,4],[6,5,7],[4,1,8,3]]
    actual = sol.minimumTotal(triangle)
    expected = 11
    assert actual == expected

def test_case_2():
    sol = Solution()
    triangle = [[-10]]
    actual = sol.minimumTotal(triangle)
    expected = -10
    assert actual == expected

if __name__ == '__main__':
    pytest.main()