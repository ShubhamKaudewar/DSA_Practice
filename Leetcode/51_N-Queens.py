from typing import List
import pytest

class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        """
        This is hard question of backtracking, video explains the logic for maintaining check against col, +/-ve diagonal
        https://www.youtube.com/watch?v=Ph95IHmRp5M
        """
        col = set()
        negDiag = set() # r-c
        posDiag = set() # r+c

        output = []
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            if r == n:
                copy = ["".join(r) for r in board]
                output.append(copy)
                return

            for c in range(n): # for each row r now check column where to place queen
                if c in col or (r+c) in posDiag or (r-c) in negDiag:
                    continue

                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r+c)
                negDiag.add(r-c)
                backtrack(r+1)

                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r+c)
                negDiag.remove(r-c)

        backtrack(0) # start from row 0
        return output


def test_case_1():
    sol = Solution()
    n = 4
    expected = [[".Q..","...Q","Q...","..Q."],["..Q.","Q...","...Q",".Q.."]]
    actual = sol.solveNQueens(n)
    assert actual == expected


def test_case_2():
    sol = Solution()
    n = 1
    expected = [["Q"]]
    actual = sol.solveNQueens(n)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()
