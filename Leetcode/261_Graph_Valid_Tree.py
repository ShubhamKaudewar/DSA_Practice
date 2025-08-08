import pytest
from typing import List
from collections import defaultdict


class Solution:
    """
    Valid tree when not cycle detected in nodes network
    """

    def valid_tree(self, n: int, edges: List[List[int]]) -> bool:
        if n == 0:
            return True

        adj_map = defaultdict(list)
        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)

        visited = set()

        def dfs(u, parent):
            visited.add(u)
            for neighbour in adj_map[u]:
                if neighbour == parent:
                    continue
                if neighbour in visited:
                    # cycle detected
                    return False
                if not dfs(neighbour, u):
                    return False
            return True

        # Start DFS from node 0
        if not dfs(0, -1):
            return False

        # Check connectivity: all nodes must be visited
        return len(visited) == n

def test_1():
    sol = Solution()
    n = 5
    edges = [[0, 1], [0, 2], [0, 3], [1, 4]]
    actual = sol.valid_tree(n, edges)
    expected = True
    assert expected == actual

def test_2():
    sol = Solution()
    n = 5
    edges = [[0, 1], [1, 2], [2, 3], [1, 3], [1, 4]]
    actual = sol.valid_tree(n, edges)
    expected = False
    assert expected == actual

def test_3():
    sol = Solution()
    n = 2
    edges = []
    actual = sol.valid_tree(n, edges)
    expected = False
    assert expected == actual

def test_4():
    sol = Solution()
    n = 1
    edges = []
    actual = sol.valid_tree(n, edges)
    expected = True
    assert expected == actual

def test_5():
    sol = Solution()
    n = 3
    edges = [[0,1]]
    actual = sol.valid_tree(n, edges)
    expected = False
    assert expected == actual

def test_6():
    sol = Solution()
    n = 8
    edges = [[0,1],[1,2],[3,2],[4,3],[4,5],[5,6],[6,7]]
    actual = sol.valid_tree(n, edges)
    expected = True
    assert expected == actual

if __name__ == "__main__":
    pytest.main()