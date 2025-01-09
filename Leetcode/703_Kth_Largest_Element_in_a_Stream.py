
import pytest
from typing import List
import heapq

class KthLargest:
    def __init__(self, k: int, nums: List[int]):
        self.k = k
        self.heap = sorted(nums)[-k:]
        heapq.heapify(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.k:
            heapq.heappop(self.heap)
        return self.heap[0]

def test_case_1():
    kl = None
    actions = ["KthLargest", "add", "add", "add", "add", "add"]
    values = [[3, [4, 5, 8, 2]], [3], [5], [10], [9], [4]]
    actual = [None]
    for action, value in zip(actions, values):
        if action == "KthLargest":
            kl = KthLargest(*value)
        elif action == "add":
            actual.append(kl.add(*value))
    expected = [None, 4, 5, 5, 8, 8]
    assert actual == expected


if __name__ == '__main__':
    pytest.main()