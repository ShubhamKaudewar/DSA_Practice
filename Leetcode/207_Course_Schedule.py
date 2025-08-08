import pytest
from typing import List
from helper import Graph


class Solution:
    """
    This is standard Kahn's Algorithm: Topological order sort problem
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        topological_order = Graph().topological_sort(numCourses, prerequisites)
        if not topological_order:
            return False
        return True


def test_1():
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    actual = sol.canFinish(numCourses, prerequisites)
    expected = True
    assert actual == expected

def test_2():
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    actual = sol.canFinish(numCourses, prerequisites)
    expected = False
    assert actual == expected

if __name__ == "__main__":
    pytest.main()