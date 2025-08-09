import pytest
from typing import List
from helper import Graph
from copy import deepcopy
from helper import UnionFind

class Solution:
    """
    This is classic problem of UnionFind,
    https://youtu.be/1lNK80tOTfc?si=c7FntBcaCCUAqOGY&t=462 check from this time that using path compression we can
    find there is already path exist between node 1 <-> 4
    """
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        uf = UnionFind(len(edges)) # This considers 0 as node
        for edge in edges:
            u, v = edge[0]-1, edge[1]-1 # Actual node value-1 are stored in parent index
            if uf.find(u) == uf.find(v): # If root parents of both the edge connected vertices is same then it is cycle
                return edge
            uf.union(u, v) # make union of two connected vertices
        return []

    """
    This can be solved in other approach using valid_tree check by removing every edge from the edges list from back side
    """
    def findRedundantConnection1(self, edges: List[List[int]]) -> List[int]:
        n = len(edges)

        for i in range(n-1, -1, -1):
            tmp = deepcopy(edges)
            tmp.pop(i)
            is_tree = Graph().valid_tree(n, tmp, root=1)
            if is_tree:
                return edges[i]
        return []


def test_1():
    sol = Solution()
    edges = [[1,2],[1,3],[2,3]]
    actual = sol.findRedundantConnection(edges)
    expected = [2,3]
    assert actual == expected

def test_2():
    sol = Solution()
    edges = [[1,2],[2,3],[3,4],[1,4],[1,5]]
    actual = sol.findRedundantConnection(edges)
    expected = [1,4]
    assert actual == expected

if __name__ == "__main__":
    pytest.main()