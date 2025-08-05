import pytest
from helper.Graph import GraphNode, Graph
from typing import Optional

class Solution:
    def cloneGraph(self, node: Optional[GraphNode]) -> Optional[GraphNode]:
        orgToClone = {} # Maintain one to one mapping of org Node to clone Node, help to check if node visited

        def clone(org):
            if org in orgToClone:
                return orgToClone[org] # Return node if already visited and have mapped clone

            clone_node = GraphNode(val=org.val)
            orgToClone[org] = clone_node # Update clone node mapping
            for nei in org.neighbors: # For each neighbour of original node copy append to clone neighbour list
                clone_node.neighbors.append(clone(nei))
            return clone_node

        return clone(node) if node else None


def test_1():
    sol = Solution()
    graph = Graph()
    adjList = [[2,4],[1,3],[2,4],[1,3]]
    node = graph.adjList_to_graph(adjList)
    clone_node = sol.cloneGraph(node)
    assert graph.is_similar(node, clone_node) == True
#
def test_2():
    sol = Solution()
    graph = Graph()
    adjList = [[]]
    node = graph.adjList_to_graph(adjList)
    clone_node = sol.cloneGraph(node)
    assert graph.is_similar(node, clone_node) == True

def test_3():
    sol = Solution()
    graph = Graph()
    adjList = []
    node = graph.adjList_to_graph(adjList)
    clone_node = sol.cloneGraph(node)
    assert graph.is_similar(node, clone_node) == True

if __name__ == "__main__":
    pytest.main()
