from typing import List
import pytest
from collections import deque

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        dq = deque()
        result = []

        for i in range(len(nums)):
            curr_val = nums[i]
            while dq and dq[0][0] <= i - k:
                dq.popleft()

            while dq and curr_val > dq[-1][1]:
                dq.pop()
            dq.append((i, nums[i]))
            if i >= k-1:
                result.append(dq[0][1])
        return result

def test_case_1():
    sol = Solution()
    assert sol.maxSlidingWindow([1,3,-1,-3,5,3,6,7], 3) == [3,3,5,5,6,7]

def test_case_2():
    sol = Solution()
    assert sol.maxSlidingWindow([1], 1) == [1]

if __name__ == '__main__':
    pytest.main()