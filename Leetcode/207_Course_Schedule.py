import pytest
from typing import List, Dict

class Solution:
    """
    This question is from Detect cycle in directed graph
    Asked in ["JusPay"]
    Algorithm is explained in medium blog using approach DFS + White-Gray-Black cycle detection
    https://yuminlee2.medium.com/detect-cycle-in-a-graph-4461b6000845
    """

    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = self.graphBuilder(numCourses, prerequisites)

        visiting = set()
        visited = set()

        for node in range(numCourses):
            if self.detectCycle(graph, node, visiting, visited):
                return False

        return len(visited) == numCourses

    def detectCycle(self, graph, node, visiting, visited):
        if node in visited:
            return False

        if node in visiting:
            return True

        visiting.add(node)
        for descendant in graph[node]:
            if self.detectCycle(graph, descendant, visiting, visited):
                return True

        visited.add(node)
        visiting.remove(node)
        return False

    def graphBuilder(self, nodes: int, edges: List[List[int]]) -> Dict[int, List[int]]:
        graph = {x: [] for x in range(nodes)}
        for edge in edges:
            a, b = edge
            graph[b].append(a)
        return graph

def test_case_1():
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0]]
    expected = True
    actual = sol.canFinish(numCourses, prerequisites)
    assert actual == expected

def test_case_2():
    sol = Solution()
    numCourses = 2
    prerequisites = [[1,0],[0,1]]
    expected = False
    actual = sol.canFinish(numCourses, prerequisites)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()