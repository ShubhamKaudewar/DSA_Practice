import pytest

class Solution:
    def totalNQueens(self, n: int) -> int:
        col = set()
        negDiag = set()  # r-c
        posDiag = set()  # r+c

        count = 0
        board = [['.'] * n for _ in range(n)]

        def backtrack(r):
            nonlocal count

            if r == n:
                count += 1
                return

            for c in range(n):  # for each row r now check column where to place queen
                if c in col or (r + c) in posDiag or (r - c) in negDiag:
                    continue

                board[r][c] = "Q"
                col.add(c)
                posDiag.add(r + c)
                negDiag.add(r - c)
                backtrack(r + 1)

                board[r][c] = "."
                col.remove(c)
                posDiag.remove(r + c)
                negDiag.remove(r - c)

        backtrack(0)  # start from row 0
        return count


def test_case_1():
    sol = Solution()
    n = 4
    expected = 2
    actual = sol.totalNQueens(n)
    assert actual == expected


def test_case_2():
    sol = Solution()
    n = 1
    expected = 1
    actual = sol.totalNQueens(n)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()
