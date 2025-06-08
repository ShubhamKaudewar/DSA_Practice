import pytest
from typing import List


class TrieNode:
    def __init__(self, val=None):
        self.val = val
        self.children = {}

class Trie:
    def __init__(self):
        self.trieNode = TrieNode()
        self.result = []

    def insert(self, n: int) -> None:
        for i in range(1, n + 1):
            curr = self.trieNode
            for digit in map(int, str(i)):
                if digit not in curr.children:
                    curr.children[digit] = TrieNode(val=i if len(curr.children) == 0 else None)
                curr = curr.children[digit]
            curr.val = i  # Set val at end node

    def dfs(self, curr: TrieNode):
        if curr.val:
            self.result.append(curr.val)

        for key, val in curr.children.items():
            self.dfs(val)



class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        trie = Trie()
        trie.insert(n)
        trie.dfs(trie.trieNode)
        return trie.result

def test_case_1():
    sol = Solution()
    n = 13
    actual = sol.lexicalOrder(n)
    expected = [1, 10, 11, 12, 13, 2, 3, 4, 5, 6, 7, 8, 9]
    assert actual == expected

def test_case_2():
    sol = Solution()
    n = 2
    actual = sol.lexicalOrder(n)
    expected = [1,2]
    assert actual == expected

def test_case_3():
    sol = Solution()
    n = 1
    actual = sol.lexicalOrder(n)
    expected = [1]
    assert actual == expected

def test_case_4():
    sol = Solution()
    n = 34
    actual = sol.lexicalOrder(n)
    expected = [1, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 2, 20, 21, 22, 23, 24, 25, 26, 27, 28, 29, 3, 30, 31, 32, 33, 34, 4, 5, 6, 7, 8, 9]
    assert actual == expected


if __name__ == '__main__':
    pytest.main()