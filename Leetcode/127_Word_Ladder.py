import pytest
from typing import List
from collections import deque

class Solution:
    """
    The approach is top -> down, we start from beginWord and simultaneously keep checking all possible combinations of
    that word by changing it's one character at one place at a time. We will do bfs at each level and which ever path
    first reach at endWord will return height of path
    """
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:
        word_set = set(wordList)
        if endWord not in word_set:
            return 0

        q = deque([(beginWord, 1)])
        visited = {beginWord}
        L = len(beginWord)
        letters = 'abcdefghijklmnopqrstuvwxyz'

        while q:
            word, dist = q.popleft()
            if word == endWord:
                return dist

            for i in range(L):
                for c in letters:
                    if c == word[i]:
                        continue # From combinations of words skip original word

                    nxt = word[:i] + c + word[i + 1:]  # Replace one character at each pointer and keep checking in provided wordList and shouldn't be visited
                    if nxt in word_set and nxt not in visited:
                        visited.add(nxt)
                        q.append((nxt, dist + 1)) # Move to next child until we reach endWord
        return 0


def test_1():
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log","cog"]
    actual = sol.ladderLength(beginWord, endWord, wordList)
    expected = 5
    assert actual == expected

def test_2():
    sol = Solution()
    beginWord = "hit"
    endWord = "cog"
    wordList = ["hot","dot","dog","lot","log"]
    actual = sol.ladderLength(beginWord, endWord, wordList)
    expected = 0
    assert actual == expected

if __name__ == "__main__":
    pytest.main()