import pytest
from typing import List

class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        row = len(board[0])
        col = len(board)
        visited = [[False] * row for _ in range(col)]
        start_word = word[0]
        exist = False

        def word_search(i, j, word_lst):
            nonlocal exist
            # search in four directions

            if not word_lst:
                exist = True
                return

            # search left
            if j > 0 and word_lst[0] == board[i][j-1] and not visited[i][j-1]:
                visited[i][j-1] = True
                word_search(i, j-1, word_lst[1:])
                if exist: return
                visited[i][j-1] = False

            # search top
            if i > 0 and word_lst[0] == board[i-1][j] and not visited[i-1][j]:
                visited[i-1][j] = True
                word_search(i-1, j, word_lst[1:])
                if exist: return
                visited[i-1][j] = False

            # search right
            if j < row-1 and word_lst[0] == board[i][j+1] and not visited[i][j+1]:
                visited[i][j+1] = True
                word_search(i, j+1, word_lst[1:])
                if exist: return
                visited[i][j+1] = False

            # search bottom
            if i < col-1 and word_lst[0] == board[i+1][j] and not visited[i+1][j]:
                visited[i+1][j] = True
                word_search(i+1, j, word_lst[1:])
                visited[i+1][j] = False
            return

        for i in range(col):
            for j in range(row):
                if board[i][j] == start_word:
                    word_lst = list(word)

                    visited = [[False] * row for _ in range(col)]
                    visited[i][j] = True
                    word_search(i, j, word_lst[1:])
                    if exist: return True

        return False

def test_case_1():
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCCED"
    expected = True
    actual = sol.exist(board, word)
    assert actual == expected

def test_case_2():
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "SEE"
    expected = True
    actual = sol.exist(board, word)
    assert actual == expected

def test_case_3():
    sol = Solution()
    board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
    word = "ABCB"
    expected = False
    actual = sol.exist(board, word)
    assert actual == expected

def test_case_4():
    sol = Solution()
    board = [["A","B","C","E"],["S","F","E","S"],["A","D","E","E"]]
    word = "ABCESEEEFS"
    expected = True
    actual = sol.exist(board, word)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()