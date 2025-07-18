from pydantic.dataclasses import dataclass
from typing import List

@dataclass
class UnionFind:
    numberOfElements: int
    
    def __post_init__(self):
        self.parent = self.makeSet(self.numberOfElements)
        self.count = self.numberOfElements
        self.size = [1]*self.numberOfElements

    def makeSet(self, numberOfElements: int) -> List[int]:
        return [x for x in range(numberOfElements)]
    
    def find(self, node):
        while node != self.parent[node]:
            # Path compression
            self.parent[node] = self.parent[self.parent[node]]
            node = self.parent[node]
        return node
    
    def union(self, node1, node2):
        root1 = self.find(node1)
        root2 = self.find(node2)
        
        if root1 == root2:
            return 
        
        if root1 != root2:
            if self.size[root1] > self.size[root2]:
                self.parent[root2] = root1 # This set root1 parent root2
                self.size[root1] += 1
            else:
                self.parent[root1] = root2 # This set root2 parent root1
                self.size[root2] += 1 # Increase the size of larger set
        
        self.count -= 1 # Since node got merged it will decrease the size of overall individual node count by 1
        
                