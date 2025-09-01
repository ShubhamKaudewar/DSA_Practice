import pytest
from typing import List
import heapq
from helper import Graph

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, k: int) -> int:
        """This use little twist approach of Dijkstra's algorithm, the trick is is using (cost, city, stop) as minHeap"""
        adj_map = Graph().construct_adjacency_list_directed_weighted(flights)
        minHeap = [(0, src, 0)] # (cost, city, stops)
        min_cost = 0
        visited = dict()

        while minHeap:
            cost, city, stop = heapq.heappop(minHeap)
            if city == dst:
                return cost
            if stop > k:
                continue
            if city in visited and visited[city] <= stop:
                continue
            visited[city] = stop

            for nei_node, nei_weight in adj_map[city]:
                heapq.heappush(minHeap, (cost+nei_weight, nei_node, stop+1))

        return min_cost if min_cost else -1


def test_case_1():
    sol = Solution()
    n = 4
    flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]]
    src = 0
    dst = 3
    k = 1
    actual = sol.findCheapestPrice(n, flights, src, dst, k)
    expected = 700
    assert actual == expected

def test_case_2():
    sol = Solution()
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 1
    actual = sol.findCheapestPrice(n, flights, src, dst, k)
    expected = 200
    assert actual == expected

def test_case_3():
    sol = Solution()
    n = 3
    flights = [[0,1,100],[1,2,100],[0,2,500]]
    src = 0
    dst = 2
    k = 0
    actual = sol.findCheapestPrice(n, flights, src, dst, k)
    expected = 500
    assert actual == expected




if __name__ == '__main__':
    pytest.main()