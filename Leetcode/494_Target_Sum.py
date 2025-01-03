from typing import List
class Solution:
    def findTargetSumWays(self, nums: List[int], target: int) -> int:
        memo = {}

        def backtrack(sum, idx):
            if (sum, idx) in memo:
                return memo[(sum, idx)]

            if idx == len(nums):
                return 1 if sum == target else 0

            add = backtrack(sum + nums[idx], idx + 1)
            subtract = backtrack(sum - nums[idx], idx + 1)

            memo[(sum, idx)] = add + subtract
            return memo[(sum, idx)]
        return backtrack(0, 0)

sol = Solution()
nums = [1,1,1,1,1]
k = 3
print(sol.findTargetSumWays(nums, k))
nums = [1]
k = 1
print(sol.findTargetSumWays(nums, k))
nums = [2, 1]
k = 1
print(sol.findTargetSumWays(nums, k))