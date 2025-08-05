import pytest
from typing import List
from collections import deque

class Solution:
    """
    This question same approach of Q.286 with only difference of incrementing distance we increment minutes
    we will be maintaining dedicated matrix for pacific and atlantic tiles. We will be doing bfs on separate tiles
    starting from their edge tiles. We will be updating tile we are checking against has adjacent tile water goes to ocean and height is lower than checking one then we will flag curr to 1
    """
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:
        row, col = len(heights), len(heights[0])
        pacificTiles = [[0]*col for _ in range(row)]
        atlanticTiles = [[0]*col for _ in range(row)]
        q = deque()
        pacific_visit, atlantic_visit = set(), set()
        output = []
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(o, r, c, dr, dc):
            x, y = r+dr, c+dc
            if min(x, y) < 0 or x == row or y == col or heights[x][y] < heights[r][c]:
                return

            visit = pacific_visit if o == pacificTiles else atlantic_visit

            if (x, y) in visit:
                return

            if o[r][c]:
                o[x][y] = 1
                q.append((o, x, y))
                visit.add((x, y))

        # Atlantic Bottom and Pacific Top tiles
        for c in range(col):
            atlanticTiles[row-1][c] = 1
            q.append((atlanticTiles, row-1, c))
            pacificTiles[0][c] = 1
            q.append((pacificTiles, 0, c))

        # Atlantic Right & Pacific Left tiles
        for r in range(row):
            atlanticTiles[r][col-1] = 1
            q.append((atlanticTiles, r, col-1))
            pacificTiles[r][0] = 1
            q.append((pacificTiles, r, 0))

        while q:
            for _ in range(len(q)):
                o, r, c = q.popleft()
                for dr, dc in directions:
                    bfs(o, r, c, dr, dc)

        # After we know each pacific and atlantic tiles water path we will check against common path to know water
        # has options to go in either ocean
        for r in range(len(heights)):
            for c in range(len(heights[0])):
                if pacificTiles[r][c] and atlanticTiles[r][c]:
                    output.append([r, c])
        return output


def test_1():
    sol = Solution()
    heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
    expected = [[0,4],[1,3],[1,4],[2,2],[3,0],[3,1],[4,0]]
    actual = sol.pacificAtlantic(heights)
    assert expected == actual

def test_2():
    sol = Solution()
    heights = [[1]]
    expected = [[0,0]]
    actual = sol.pacificAtlantic(heights)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()