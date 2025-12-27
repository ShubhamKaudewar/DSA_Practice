from copy import deepcopy

import pytest
from typing import List

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        """This example of Kadane's Algorithm which need to maintain min max of subarray
        Along with this need to calculate circular_sum for circular loop"""
        total_sum = sum(nums)
        minSum, maxSum = 0, 0
        normal_max, normal_min = float('-inf'), float('inf')

        for num in nums:
            tmp = maxSum + num
            maxSum = max(num, num + maxSum, num + minSum)
            minSum = min(num, tmp, num + minSum)
            normal_min = min(normal_min, minSum)
            normal_max = max(normal_max, maxSum)

        circular_sum = total_sum - normal_min
        if max(nums) > 0:
            return max(circular_sum, normal_max)
        return normal_max

    def maxSubarraySumCircular2(self, nums: List[int]) -> int:
        n = len(nums)
        ans = float('-inf')

        for k in range(n):
            minSum, maxSum = 0, 0
            res = float('-inf')

            for i in range(n):
                curr = nums[(i+k)%n]

                tmp = maxSum + curr
                maxSum = max(curr, curr+maxSum, curr+minSum)
                minSum = min(curr, tmp, curr+minSum)
                res = max(res, maxSum)
            ans = max(ans, res)
        return ans



def test_case_1():
    sol = Solution()
    nums = [1,-2,3,-2]
    actual = sol.maxSubarraySumCircular(nums)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [5,-3,5]
    actual = sol.maxSubarraySumCircular(nums)
    expected = 10
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [-3,-2,-3]
    actual = sol.maxSubarraySumCircular(nums)
    expected = -2
    assert actual == expected

if __name__ == '__main__':
    pytest.main()