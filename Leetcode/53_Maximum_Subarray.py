import pytest
from typing import List

class Solution:
    """
        This is classic question of greedy and Kadane's algorithm
        This question can be solved using max, min maintaining. And when 0 appear resetting max & min to 0
        Kadane's Algorithm:
        The idea of Kadane's algorithm is to traverse over the array from left to right and for each element,
        find the maximum sum among all subarrays ending at that element. The result will be the maximum of all these values.
    """
    def maxSubArray(self, nums: List[int]) -> int:
        res = nums[0]
        curMax, curMin = 0, 0

        for num in nums:
            tmp = curMax + num
            curMax = max(curMax + num, curMin + num, num)
            curMin = min(num, curMin + num, tmp)
            res = max(curMax, res)
        return res

def test_case_1():
    sol = Solution()
    nums = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
    actual = sol.maxSubArray(nums)
    expected = 6
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1]
    actual = sol.maxSubArray(nums)
    expected = 1
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [5,4,-1,7,8]
    actual = sol.maxSubArray(nums)
    expected = 23
    assert actual == expected

if __name__ == '__main__':
    pytest.main()