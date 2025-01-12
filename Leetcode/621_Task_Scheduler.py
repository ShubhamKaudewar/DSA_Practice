import pytest
from typing import Optional, List
import heapq, math
import collections

class Solution:
    def decrement(self, idle):
        for k in list(idle.keys()):
            idle[k] -= 1
        return idle

    def leastInterval(self, tasks: List[str], n: int) -> int:
        c = collections.Counter(tasks)
        heap = [(v, k) for k, v in dict(c).items()]
        heapq.heapify(heap)

        sequence = []
        idle = collections.defaultdict(lambda: 0)

        while heap:
            for i in range(1, len(heap)+1):
                large = heapq.nlargest(i, heap)
                if idle.get(large) == 0:
                    sequence.append(large[1])
                    idle[large] = n
                    heapq
        return len(sequence)

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