from collections import defaultdict

import pytest
from typing import List
from helper import Graph
from heapq import heappop, heappush

class Solution:
    def minCostConnectPoints(self, points: List[List[int]]) -> int:
        """This is classic question of Prim's algorithm, to use Minimum Spanning Tree (MST) and visited node approach"""
        edges = []
        for idx, point in enumerate(points):
            edges.extend([[tuple(point), tuple(x), abs(x[0]-point[0])+abs(x[-1]-point[-1])] for x in points[idx+1::]])


        adj_map = Graph().construct_adjacency_list_bidirected_weighted(edges)
        MST = [(0, tuple(points[0]))] # we will start from 1st point
        min_cost = 0
        visited = set()

        # while MST: # this is also correct
        while len(visited) != len(points):
            weight, node = heappop(MST)
            if node in visited:
                continue

            visited.add(node)
            min_cost += weight

            for nei_node, nei_weight in adj_map[node]:
                if nei_node in visited:
                    continue

                heappush(MST, (nei_weight, nei_node))

        return min_cost



def test_case_1():
    sol = Solution()
    points = [[0,0],[2,2],[3,10],[5,2],[7,0]]
    actual = sol.minCostConnectPoints(points)
    expected = 20
    assert actual == expected

def test_case_2():
    sol = Solution()
    points = [[3,12],[-2,5],[-4,1]]
    actual = sol.minCostConnectPoints(points)
    expected = 18
    assert actual == expected



if __name__ == '__main__':
    pytest.main()