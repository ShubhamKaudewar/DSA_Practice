from typing import List
import pytest

class Solution:
    """
    Exact Solution of Q. 1011 also works here
    """
    def splitArray(self, nums: List[int], k: int) -> int:
        def canSplit(nums, k, maxSum):
            currentSum = 0
            splits = 1
            for num in nums:
                if currentSum + num > maxSum:
                    splits += 1
                    currentSum = num
                    if splits > k:
                        return False
                else:
                    currentSum += num
            return True

        low, high = max(nums), sum(nums)
        while low < high:
            mid = (low + high) // 2
            if canSplit(nums, k, mid):
                high = mid
            else:
                low = mid + 1
        return low


def test_case_1():
    sol = Solution()
    assert sol.splitArray([7,2,5,10,8], 2) == 18

def test_case_2():
    sol = Solution()
    assert sol.splitArray([1,2,3,4,5], 2) == 9

def test_case_3():
    sol = Solution()
    assert sol.splitArray([1,4,4], 3) == 4

if __name__ == '__main__':
    pytest.main()