import pytest
from typing import List
from heapq import heappop, heappush

class Solution:
    def swimInWater(self, grid: List[List[int]]) -> int:
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
        n = len(grid)

        minHeap = [(grid[0][0], 0, 0)] # maxEvelatedSoFar, x, y
        visited = set()

        while minHeap:
            maxElevation, x, y = heappop(minHeap)
            if (x, y) in visited:
                continue

            if x == n-1 and y == n-1:
                return maxElevation
            visited.add((x, y))

            # Let's go in neighbour tiles; core of Dijkstra's algo
            for dx, dy in directions:
                nx, ny = dx+x, dy+y
                if 0 <= nx < n and 0 <= ny < n and (nx, ny) not in visited:
                    maxElev = max(grid[ny][nx], maxElevation)
                    heappush(minHeap, (maxElev, nx, ny))
        return -1




def test_case_1():
    sol = Solution()
    grid = [[0,2],[1,3]]
    actual = sol.swimInWater(grid)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    grid = [[0,1,2,3,4],[24,23,22,21,5],[12,13,14,15,16],[11,17,18,19,20],[10,9,8,7,6]]
    actual = sol.swimInWater(grid)
    expected = 16
    assert actual == expected



if __name__ == '__main__':
    pytest.main()