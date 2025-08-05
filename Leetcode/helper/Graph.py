from __future__ import annotations
from pydantic import BaseModel, Field
from typing import List, Optional
from collections import deque

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


GraphNode.model_rebuild()