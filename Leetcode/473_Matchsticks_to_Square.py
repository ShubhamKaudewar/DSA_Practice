import pytest
from typing import List

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        perimeter = sum(matchsticks)
        if perimeter % 4 != 0:
            return False

        width = perimeter//4

        matchsticks.sort(reverse=True)
        matches = 4

        def dfs(size, arr):
            nonlocal matches

            if size > width:
                return False
            if size == width:
                matches -= 1
                return True

            i = 0
            while arr:
                if i >= len(arr):
                    break

                edge = arr.pop(i)
                fit = dfs(size+edge, arr)
                if fit:
                    i = 0
                else:
                    arr.insert(0, edge)
                    i += 1

            if matches:
                return False
            return True

        return dfs(0, matchsticks)


# def test_case_1():
#     sol = Solution()
#     matchsticks = [1,1,2,2,2]
#     actual = sol.makesquare(matchsticks)
#     expected = True
#     assert actual == expected
#
# def test_case_2():
#     sol = Solution()
#     matchsticks = [3,3,3,3,4]
#     actual = sol.makesquare(matchsticks)
#     expected = False
#     assert actual == expected

def test_case_3():
    sol = Solution()
    matchsticks = [5,5,5,5,4,4,4,4,3,3,3,3]
    actual = sol.makesquare(matchsticks)
    expected = True
    assert actual == expected

if __name__ == '__main__':
    pytest.main()