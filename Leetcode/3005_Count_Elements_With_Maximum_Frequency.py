from typing import List
import pytest
from collections import Counter
import heapq

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        freq = Counter(nums)
        heap = []
        ans = 0
        for k, v in freq.items():
            heapq.heappush(heap, -v)

        max_val = heapq.heappop(heap)
        ans += max_val
        while heap:
            val = heapq.heappop(heap)
            if val != max_val:
                break
            ans += val
        return -ans

def test_case_1():
    sol = Solution()
    nums = [1,2,2,3,1,4]
    actual = sol.maxFrequencyElements(nums)
    expected = 4
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,2,3,4,5]
    actual = sol.maxFrequencyElements(nums)
    expected = 5
    assert actual == expected

if __name__ == '__main__':
    pytest.main()