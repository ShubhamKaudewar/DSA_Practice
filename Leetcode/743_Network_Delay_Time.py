import pytest
from typing import List
import heapq
from helper import Graph

class Solution:
    def networkDelayTime(self, times: List[List[int]], n: int, k: int) -> int:
        adj_map = Graph().construct_adjacency_list_directed_weighted(times)
        minHeap = [(0, k)]
        visited = set()
        min_time = 0

        while minHeap:
            weight, node = heapq.heappop(minHeap)
            if node in visited:
                continue
            visited.add(node)
            min_time = max(min_time, weight)

            for nei_node, nei_weight in adj_map[node]:
                if nei_node in visited:
                    continue

                heapq.heappush(minHeap, (min_time + nei_weight, nei_node))

        return min_time if len(visited) == n else -1


def test_case_1():
    sol = Solution()
    times = [[2, 1, 1], [2, 3, 1], [3, 4, 1]]
    n = 4
    k = 2
    actual = sol.networkDelayTime(times, n, k)
    expected = 2
    assert actual == expected

def test_case_2():
    sol = Solution()
    times = [[1,2,1]]
    n = 2
    k = 1
    actual = sol.networkDelayTime(times, n, k)
    expected = 1
    assert actual == expected

def test_case_3():
    sol = Solution()
    times = [[1,2,1]]
    n = 2
    k = 2
    actual = sol.networkDelayTime(times, n, k)
    expected = -1
    assert actual == expected

def test_case_4():
    sol = Solution()
    times = [[1,2,1],[2,3,2],[1,3,1]]
    n = 3
    k = 2
    actual = sol.networkDelayTime(times, n, k)
    expected = -1
    assert actual == expected




if __name__ == '__main__':
    pytest.main()