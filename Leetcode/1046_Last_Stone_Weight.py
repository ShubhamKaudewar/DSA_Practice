
import pytest
from typing import List
import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        if stones and len(stones) > 1:
            heap = [-stone for stone in stones]
            heapq.heapify(heap)
        else:
            return stones[-1] if stones else 0

        while len(heap) > 1:
            first_large = heapq.heappop(heap)
            second_large = heapq.heappop(heap)
            if first_large == second_large:
                continue
            else:
                remain = abs(first_large - second_large)
                heapq.heappush(heap, -remain)
        return -1*heap[-1] if heap else 0

def test_case_1():
    sol = Solution()
    stones = [2,7,4,1,8,1]
    actual = sol.lastStoneWeight(stones)
    expected = 1
    assert actual == expected

if __name__ == '__main__':
    pytest.main()