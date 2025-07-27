import collections
from typing import List
import pytest

class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:
        if not grid:
            return 0

        visit = set()
        rows, cols = len(grid), len(grid[0])
        max_area = 0

        def bfs(r, c, area):
            visit.add((r, c))
            q = collections.deque()
            q.append((r, c))

            while q:
                row, col = q.popleft()
                directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]

                for dr, dc in directions:
                    r, c = row + dr, col + dc
                    if 0 <= r < rows and 0 <= c < cols and (r, c) not in visit and grid[r][c]:
                        q.append((r, c))
                        visit.add((r, c))
                        area = bfs(r, c, area+1)
            return area

        for r in range(rows):
            for c in range(cols):
                if grid[r][c] and (r, c) not in visit:
                    area = bfs(r, c, 1)
                    max_area = max(max_area, area)
        return max_area


def test_case_1():
    sol = Solution()
    grid = [[0, 0, 1, 0, 0, 0, 0, 1, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 1, 1, 0, 1, 0, 0, 0, 0, 0, 0, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 0, 1, 0, 0],
            [0, 1, 0, 0, 1, 1, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 1, 1, 0, 0, 0, 0]]
    expected = 6
    actual = sol.maxAreaOfIsland(grid)
    assert actual == expected

def test_case_2():
    sol = Solution()
    grid = [[0,0,0,0,0,0,0,0]]
    expected = 0
    actual = sol.maxAreaOfIsland(grid)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()
