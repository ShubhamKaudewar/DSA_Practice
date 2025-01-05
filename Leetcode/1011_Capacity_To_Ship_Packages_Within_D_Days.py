from typing import List
import pytest

class Solution:
    """
    This is very slow solution passing almost edge of acceptable
    """
    def shipWithinDays(self, weights: List[int], days: int) -> int:
        prefixSum = [0] * (len(weights) + 1)
        for i in range(1, len(weights)+1):
            prefixSum[i] = weights[i-1] + prefixSum[i-1]
        prefixSum.pop(0)

        def checkDays(limit):
            nonlocal weights
            required = 0
            i = 0
            capacity = limit
            while i < len(weights):
                if capacity >= weights[i]:
                    capacity -= weights[i]
                    i += 1
                if i == len(weights) or capacity < weights[i]:
                    required += 1
                    capacity = limit
            return required

        min_required = max(weights)
        left, right = min_required, prefixSum[-1]
        min_size = 0

        while left <= right:
            mid = left + (right - left)//2
            if prefixSum[-1] < min_required:
                required = float('inf')
            else:
                required = checkDays(mid)
            if required <= days:
                min_size = mid
                right = mid - 1
            else:
                left = mid + 1
        return min_size


def test_case_1():
    sol = Solution()
    assert sol.shipWithinDays([1,2,3,4,5,6,7,8,9,10], 5) == 15

def test_case_2():
    sol = Solution()
    assert sol.shipWithinDays([3,2,2,4,1,4], 3) == 6

def test_case_3():
    sol = Solution()
    assert sol.shipWithinDays([1,2,3,1,1], 4) == 3

if __name__ == '__main__':
    pytest.main()