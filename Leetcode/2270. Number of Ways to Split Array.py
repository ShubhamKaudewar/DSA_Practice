from typing import List

class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefixSum = [0] * (len(nums) + 1)
        for i in range(len(nums)):
            prefixSum[i+1] = prefixSum[i] + nums[i]

        total_sum = prefixSum[-1]
        count = 0
        for i in range(1, len(prefixSum)-1):
            if prefixSum[i] >= total_sum - prefixSum[i]:
                count += 1
        return count

if __name__ == '__main__':
    sol = Solution()
    nums = [10,4,-8,7]
    print(sol.waysToSplitArray(nums) == 2)
    nums = [2,3,1,0]
    print(sol.waysToSplitArray(nums) == 2)
    # nums = [10,4,-8,7]
    # print(sol.waysToSplitArray(nums) == 2)