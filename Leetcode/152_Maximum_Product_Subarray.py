import pytest
from typing import List

class Solution:
    """
        This question can be solved using max, min maintaining. And when 0 appear reseting max & min to 1
        Kadane's Algorithm:
        The idea of Kadane's algorithm is to traverse over the array from left to right and for each element,
        find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values.
    """

    def maxProduct(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 1, 1

        for num in nums:
            tmp = curMax * num
            curMax = max(curMax * num, curMin * num, num)
            curMin = min(num, curMin * num, tmp)
            res = max(curMax, res)
        return res


def test_1():
    sol = Solution()
    nums = [2,3,-2,4]
    expected = 6
    actual = sol.maxProduct(nums)
    assert expected == actual

def test_2():
    sol = Solution()
    nums = [-2,0,-1]
    expected = 0
    actual = sol.maxProduct(nums)
    assert expected == actual

def test_3():
    sol = Solution()
    nums = [0, 10, 10, 10, 10, 10, 10, 10, 10, 10, -10, 10, 10, 10, 10, 10, 10, 10, 10, 10, 0]
    expected = 1000000000
    actual = sol.maxProduct(nums)
    assert expected == actual


if __name__ == "__main__":
    pytest.main()