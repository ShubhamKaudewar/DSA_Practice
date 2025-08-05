import pytest
from typing import List
from collections import deque


class Solution:
    """
    This question follows the same multi-source BFS approach as Q.286 (Walls and Gates),
    but instead of propagating distance, we mark edge-connected 'O's to avoid flipping.
    """

    def solve(self, board: List[List[str]]) -> None:
        if not board or not board[0]:
            return

        row, col = len(board), len(board[0])
        q = deque()
        avoid = set()
        directions = [(-1, 0), (0, 1), (1, 0), (0, -1)]

        def bfs(r, c):
            if 0 <= r < row and 0 <= c < col and board[r][c] == "O" and (r, c) not in avoid:
                q.append((r, c))
                avoid.add((r, c))

        # Add all border 'O's to queue
        for c in range(col):
            if board[0][c] == "O":
                bfs(0, c)
            if board[row - 1][c] == "O":
                bfs(row - 1, c)

        for r in range(row):
            if board[r][0] == "O":
                bfs(r, 0)
            if board[r][col - 1] == "O":
                bfs(r, col - 1)

        # Multi-source BFS to find all connected 'O's
        while q:
            r, c = q.popleft()
            for dr, dc in directions:
                bfs(r + dr, c + dc)

        # Flip all non-avoided 'O's to 'X'
        for r in range(row):
            for c in range(col):
                if (r, c) not in avoid and board[r][c] == "O":
                    board[r][c] = "X"


def test_1():
    sol = Solution()
    board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
    expected = [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
    sol.solve(board)
    assert expected == board

def test_2():
    sol = Solution()
    board = [["X"]]
    expected = [["X"]]
    sol.solve(board)
    assert expected == board

def test_3():
    sol = Solution()
    board = [["X"]]
    expected = [["X"]]
    sol.solve(board)
    assert expected == board

if __name__ == "__main__":
    pytest.main()