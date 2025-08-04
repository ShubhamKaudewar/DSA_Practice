import pytest
from typing import List


class Solution:
    def canPartition(self, nums: List[int]) -> bool:
        totalSum = sum(nums)
        if totalSum % 2 == 1:
            return False

        targetSum = totalSum // 2
        dp = [False] * (targetSum+1)
        dp[0] = True

        for num in nums:
            for i in range(targetSum, num-1, -1):
                if dp[i-num]: # for 1 (because of 0 we flag true), when i become 6 and num 5 6-5 we hae flagged True like this algorithm goes
                    dp[i] = True
        return dp[targetSum]

def test_1():
    sol = Solution()
    nums = [1,5,11,5]
    expected = True
    actual = sol.canPartition(nums)
    assert expected == actual

def test_2():
    sol = Solution()
    nums = [1,2,3,5]
    expected = False
    actual = sol.canPartition(nums)
    assert expected == actual


if __name__ == "__main__":
    pytest.main()