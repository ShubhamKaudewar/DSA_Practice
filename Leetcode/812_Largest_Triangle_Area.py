from typing import List
import pytest
from itertools import combinations

class Solution:
    def largestTriangleArea(self, points: List[List[int]]) -> float:
        """
        Find all combinations of 3 vertices of triangle and find maximum area among those.
        """
        area = 0
        for vertex in combinations(points, 3):
            x1, y1 = vertex[0]
            x2, y2 = vertex[1]
            x3, y3 = vertex[2]
            area = max(area, (1/2) * abs(x1 * (y2 - y3) + x2 * (y3 - y1) + x3 * (y1 - y2)))
        return float(area)


def test_case_1():
    sol = Solution()
    points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
    actual = sol.largestTriangleArea(points)
    expected = 2.00000
    assert actual == expected

def test_case_2():
    sol = Solution()
    points = [[1,0],[0,0],[0,1]]
    actual = sol.largestTriangleArea(points)
    expected = 0.50000
    assert actual == expected

if __name__ == '__main__':
    pytest.main()