from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional, Dict, Any
from collections import deque, defaultdict
import pytest

class GraphNode(BaseModel):
    val: int
    neighbors: List[GraphNode] = Field(default_factory=list)
    __hash__ = object.__hash__

class Graph:
    def adjList_to_graph(self, adjList: List[List[int]]) -> Optional[GraphNode, None]:
        if not adjList or not adjList[0]:
            return None

        nodes = [GraphNode(val=i + 1) for i in range(len(adjList))]
        for i, neighbors in enumerate(adjList):
            nodes[i].neighbors = [nodes[n - 1] for n in neighbors]
        return nodes[0]

    @staticmethod
    def is_similar(node1: GraphNode, node2: GraphNode) -> bool:
        # Check if both references point to the exact same object (memory address)
        if not node1 and not node2:
            return True

        if id(node1) == id(node2):
            # They are the same object reference, so not considered similar distinct graphs
            return False

        # Existing BFS or DFS logic to compare structure and values
        # (similar to earlier provided method)
        visited1 = {}
        visited2 = {}

        from collections import deque
        queue = deque([(node1, node2)])
        while queue:
            n1, n2 = queue.popleft()

            if n1 is None or n2 is None:
                if n1 != n2:
                    return False
                continue

            if id(n1) in visited1 or id(n2) in visited2:
                if id(n1) in visited1 and id(n2) in visited2:
                    continue
                else:
                    return False

            if n1.val != n2.val or len(n1.neighbors) != len(n2.neighbors):
                return False

            visited1[id(n1)] = n1
            visited2[id(n2)] = n2

            n1_neighbors = sorted(n1.neighbors, key=lambda x: x.val)
            n2_neighbors = sorted(n2.neighbors, key=lambda x: x.val)

            for nb1, nb2 in zip(n1_neighbors, n2_neighbors):
                queue.append((nb1, nb2))

        return True


    def construct_adjacency_list(self, V: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        adj_map = defaultdict(list)
        for u, v in edges:
            adj_map[u].append(v)
        for i in range(V):
            adj_map.setdefault(i, [])
        return adj_map


    def topological_sort(self, V: int, edges: List[List[int]]) -> List[int]:
        adj_map = self.construct_adjacency_list(V, edges)
        neighbours = defaultdict(int)
        topological_order = []

        for v_list in adj_map.values():
            for vertex in v_list :
                neighbours[vertex] += 1


        q = deque()
        for i in range(V):
            if neighbours[i] == 0:
                q.append(i)

        def bfs(u):
            for v in adj_map[u]:
                neighbours[v] -= 1
                if neighbours[v] == 0:
                    q.append(v)

        while q:
            vertex = q.popleft()
            bfs(vertex)
            topological_order.append(vertex)

        if len(topological_order) != V:
            return []
        return topological_order


GraphNode.model_rebuild()


def test_1():
    g = Graph()
    V = 6
    edges = [[0, 1], [1, 2], [2, 3], [4, 5], [5, 1], [5, 2]]
    actual = g.topological_sort(V, edges)
    expected = [0, 4, 5, 1, 2, 3]
    assert expected == actual

if __name__ == "__main__":
    pytest.main()
