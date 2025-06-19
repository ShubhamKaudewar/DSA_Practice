import pytest
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[int]) -> List[int]:
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
    assert set(actual) == set(expected)

def test_case_2():
    sol = Solution()
    numCourses = 4
    prerequisites = [[1,0],[2,0],[3,1],[3,2]]
    expected = [0,2,1,3]
    actual = sol.findOrder(numCourses, prerequisites)
    assert set(actual) == set(expected)

if __name__ == '__main__':
    pytest.main()