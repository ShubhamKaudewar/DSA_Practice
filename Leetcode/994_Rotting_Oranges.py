import pytest
from typing import List
from collections import deque

class Solution:
    """
    This question same approach of Q.286 with only difference of incrementing distance we increment minutes
    """
    def orangesRotting(self, grid: List[List[int]]) -> int:
        row, col = len(grid), len(grid[0])
        q = deque()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(r, c):
            if min(r, c) < 0 or r == row or c == col or grid[r][c] != 1:
                return

            grid[r][c] = 2
            q.append((r, c))

        for r in range(row):
            for c in range(col):
                if grid[r][c] == 2:
                    q.append((r, c))

        mins = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()

                for dx, dy in directions:
                    bfs(r + dx, c + dy)
            mins += 1

        # check if any fresh fruit remains
        for row in grid:
            if 1 in row:
                return -1

        return max(mins-1, 0)


def test_1():
    sol = Solution()
    grid = [[2,1,1],[1,1,0],[0,1,1]]
    expected = 4
    actual = sol.orangesRotting(grid)
    assert expected == actual

def test_2():
    sol = Solution()
    grid = [[2,1,1],[0,1,1],[1,0,1]]
    expected = -1
    actual = sol.orangesRotting(grid)
    assert expected == actual

def test_3():
    sol = Solution()
    grid = [[0,2]]
    expected = 0
    actual = sol.orangesRotting(grid)
    assert expected == actual

def test_4():
    sol = Solution()
    grid = [[0]]
    expected = 0
    actual = sol.orangesRotting(grid)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()