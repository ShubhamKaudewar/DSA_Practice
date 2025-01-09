import pytest
from typing import Optional, List
import heapq, math


class Solution:

    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = []
        heapq.heapify(heap)
        for pair in points:
            dist = math.sqrt(pair[0]**2 + pair[1]**2)
            heapq.heappush(heap, (dist, pair))

        k_closest = []
        for _ in range(k):
            popped = heapq.heappop(heap)
            k_closest.append(list(popped[1]))
        return k_closest


def test_case_1():
    sol = Solution()
    points, k = [[1,3],[-2,2]], 1
    expected = [[-2,2]]
    actual = sol.kClosest(points, k)
    assert actual == expected

def test_case_2():
    sol = Solution()
    points, k = [[3,3],[5,-1],[-2,4]], 2
    expected = [[3,3],[-2,4]]
    actual = sol.kClosest(points, k)
    assert actual == expected

def test_case_3():
    sol = Solution()
    points, k = [[9997,9997],[9996,9998]], 1
    expected = [[9997,9997]]
    actual = sol.kClosest(points, k)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()