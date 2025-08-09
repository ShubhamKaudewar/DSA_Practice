from typing import List
import pytest
from collections import defaultdict
import heapq

class Solution:
    """Below solution work but get TLE for because of for loop over interval and queries which is O(NxQ)"""
    def minInterval1(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        heap_map = defaultdict(lambda: float('inf'))

        for start, end in intervals:
            size = end-start+1
            for query in queries:
                if start <= query <= end:
                    heap_map[query] = min(heap_map[query], size)

        output = []
        for query in queries:
            output.append(heap_map.get(query, -1))
        return output

    def minInterval(self, intervals: List[List[int]], queries: List[int]) -> List[int]:
        intervals.sort()
        sorted_queries = sorted((q, i) for i, q in enumerate(queries))
        res = [-1] * len(queries)
        min_heap = []
        i = 0

        for q, idx in sorted_queries:
            # Add all intervals starting before or at query
            while i < len(intervals) and intervals[i][0] <= q:
                l, r = intervals[i]
                heapq.heappush(min_heap, (r - l + 1, r))
                i += 1

            # Remove intervals that end before query
            while min_heap and min_heap[0][1] < q:
                heapq.heappop(min_heap)

            # If heap is not empty, top is the smallest valid interval
            if min_heap:
                res[idx] = min_heap[0][0]

        return res

def test_case_1():
    sol = Solution()
    intervals = [[1,4],[2,4],[3,6],[4,4]]
    queries = [2,3,4,5]
    expected = [3,3,1,4]
    actual = sol.minInterval(intervals, queries)
    assert actual == expected

def test_case_2():
    sol = Solution()
    intervals = [[2,3],[2,5],[1,8],[20,25]]
    queries = [2,19,5,22]
    expected = [2,-1,4,6]
    actual = sol.minInterval(intervals, queries)
    assert actual == expected

def test_case_3():
    sol = Solution()
    intervals = [[4,5],[5,8],[1,9],[8,10],[1,6]]
    queries = [7,9,3,9,3]
    expected = [4,3,6,3,6]
    actual = sol.minInterval(intervals, queries)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()