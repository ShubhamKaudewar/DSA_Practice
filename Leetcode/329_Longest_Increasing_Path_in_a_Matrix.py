import collections
import pytest
from typing import List

class Solution:
    """
    This is 2DP question, we will start from 1st cell and keep visiting all cell who are greater than parent cell
    This way we will be increasing parent_cell_longest_path = 1 + child_cell_longest_path, by maintaining cache
    """
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix or not matrix[0]:
            return 0

        rows, cols = len(matrix), len(matrix[0])
        memo = [[0] * cols for _ in range(rows)]

        def dfs(r, c):
            if memo[r][c]:
                return memo[r][c]

            directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]
            max_len = 1

            for dr, dc in directions:
                nr, nc = r + dr, c + dc
                if 0 <= nr < rows and 0 <= nc < cols and matrix[nr][nc] > matrix[r][c]:
                    max_len = max(max_len, 1 + dfs(nr, nc))

            memo[r][c] = max_len
            return memo[r][c]

        longest = 0
        for r in range(rows):
            for c in range(cols):
                longest = max(longest, dfs(r, c))
        return longest


def test_case_1():
    sol = Solution()
    matrix = [[9,9,4],[6,6,8],[2,1,1]]
    expected = 4
    actual = sol.longestIncreasingPath(matrix)
    assert actual == expected

def test_case_2():
    sol = Solution()
    matrix = [[3,4,5],[3,2,6],[2,2,1]]
    expected = 4
    actual = sol.longestIncreasingPath(matrix)
    assert actual == expected

def test_case_3():
    sol = Solution()
    matrix = [[1]]
    expected = 1
    actual = sol.longestIncreasingPath(matrix)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()

