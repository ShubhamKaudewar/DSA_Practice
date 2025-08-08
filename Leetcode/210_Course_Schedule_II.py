import pytest
from typing import List
from helper import Graph

class Solution:
    """
    This is standard Kahn's Algorithm: Topological order sort problem
    """
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        prerequisites = [prerequisite[::-1] for prerequisite in prerequisites]
        topological_order = Graph().topological_sort(numCourses, prerequisites)
        return topological_order

    """
    This Question can be solved using other approach, which is maintaining set of vising and visited vertex
    """
    def findOrder1(self, numCourses: int, prerequisites: List[int]) -> List[int]:
        prereq = {c: [] for c in range(numCourses)}
        for crs, pre in prerequisites:
            prereq[crs].append(pre)

        output = []
        visited, visiting = set(), set()

        def dfs(crs):
            if crs in visiting:
                return False
            if crs in visited:
                return True

            visiting.add(crs)
            for pre in prereq[crs]:
                if not dfs(pre):
                    return False

            visiting.remove(crs)
            visited.add(crs)
            output.append(crs)
            return True

        for c in range(numCourses):
            if not dfs(c):
                return []
        return output



def test_case_1():
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    expected = [0,1]
    actual = sol.findOrder(numCourses, prerequisites)
    assert actual == expected

def test_case_2():
    sol = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    expected = [0,1,2,3]
    actual = sol.findOrder(numCourses, prerequisites)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()