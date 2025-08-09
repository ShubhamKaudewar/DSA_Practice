import pytest
from typing import List
from collections import defaultdict

class Solution:
    """
    Imagine the graph as a network:
    If you can travel from one node to another by following edges, they belong to the same connected component.
    If there’s no path between two groups of nodes, they form separate components.
    """
    def count_components(self, n: int, edges: List[List[int]]) -> int:
        if n == 0:
            return 0

        adj_map = defaultdict(list)
        for u, v in edges:
            adj_map[u].append(v)
            adj_map[v].append(u)

        components = 0
        visited = set()
        def dfs(child):
            if child in visited:
                return
            visited.add(child)

            for neighbour in adj_map[child]:
                dfs(neighbour)

        for node in range(n):
            if node in visited:
                continue
            else:
                components += 1
                dfs(node)
        return components


def test_1():
    sol = Solution()
    n = 3
    edges = [[0,1], [0,2]]
    actual = sol.count_components(n, edges)
    expected = 1
    assert actual == expected

def test_2():
    sol = Solution()
    n = 6
    edges = [[0,1], [1,2], [2, 3], [4, 5]]
    actual = sol.count_components(n, edges)
    expected = 2
    assert actual == expected

def test_3():
    sol = Solution()
    n = 3
    edges = [[0, 2]]
    actual = sol.count_components(n, edges)
    expected = 2
    assert actual == expected

if __name__ == "__main__":
    pytest.main()