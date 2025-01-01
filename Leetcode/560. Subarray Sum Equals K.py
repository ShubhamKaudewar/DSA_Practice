from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        k_sum = [0] * (len(nums) + 1)
        for idx, num in enumerate(nums):
            k_sum[idx+1] = k_sum[idx] + num

        res = 0
        for i in range(len(k_sum)):
            for j in range(i+1, len(k_sum)):
                if k_sum[j] - k_sum[i] == k:
                    res += 1
        return res

if __name__ == '__main__':
    sol = Solution()
    nums, k = [1,1,1], 2
    # nums, k = [1,2,3], 3
    print(sol.subarraySum(nums, k))