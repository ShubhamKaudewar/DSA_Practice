from typing import List
import pytest
from functools import cache

class Solution:
    def twoEggDrop(self, n: int) -> int:

        @cache
        def dfs(floor):
            if floor == 1:
                return 1

            mini = float('inf')
            for i in range(1, floor):
                # if egg break, that means you have to come up from 1 to i - 1,
                # so i - 1 required future attempt + 1 for the current action
                egg_break = i

                # not break
                not_break = 1 + dfs(floor - i)
                # take max because we are not sure it will break or not, so we need to keep it
                # min is just tell us which floor to start with will be minimal
                mini = min(mini, max(egg_break, not_break))

            return mini

        return dfs(n)

def test_case_1():
    sol = Solution()
    n = 2
    actual = sol.twoEggDrop(n)
    expected = 2
    assert actual == expected

def test_case_2():
    sol = Solution()
    n = 100
    actual = sol.twoEggDrop(n)
    expected = 14
    assert actual == expected


if __name__ == '__main__':
    pytest.main()