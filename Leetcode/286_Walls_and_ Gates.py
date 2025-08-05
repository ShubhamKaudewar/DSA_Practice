import pytest
from typing import List
from collections import deque

class Solution:
    """
    This is classic problem of bfs, we will start simultaneously from gates to find the nearest inf space and mark with
    the distance from gates.
    https://youtu.be/e69C6xhiSQE?si=_pg5hGVxCvJ3-PG-&t=240
    https://www.lintcode.com/problem/663/
    """
    def walls_and_gates(self, rooms: List[List[int]]) -> List[List[int]]:
        row, col = len(rooms), len(rooms[0])
        q = deque()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)] # From gates and then next close dist we will go in all directions

        def bfs(r, c, dist):
            if min(r, c) < 0 or r == row or c == col or rooms[r][c] != 2147483647: #  if a cell value is not INF, it means the cell is one of: {gate, wall, a cell with the shortest distance updated already}, we won't visit the cell again
                return

            rooms[r][c] = dist
            q.append((r, c)) # after gate we will start going in all direction from tile of dist 1 so adding those in stack


        for r in range(row):
            for c in range(col):
                if rooms[r][c] == 0:
                    q.append((r, c))

        dist = 0
        while q:
            for _ in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = dist
                for dx, dy in directions:
                    bfs(r+dx, c+dy, dist)
            dist += 1

        return rooms


def test_1():
    sol = Solution()
    rooms = [[2147483647,-1,0,2147483647],[2147483647,2147483647,2147483647,-1],[2147483647,-1,2147483647,-1],[0,-1,2147483647,2147483647]]
    expected = [[3,-1,0,1],[2,2,1,-1],[1,-1,2,-1],[0,-1,3,4]]
    actual = sol.walls_and_gates(rooms)
    assert expected == actual

def test_2():
    sol = Solution()
    rooms = [[0,-1],[2147483647,2147483647]]
    expected = [[0,-1],[1,2]]
    actual = sol.walls_and_gates(rooms)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()