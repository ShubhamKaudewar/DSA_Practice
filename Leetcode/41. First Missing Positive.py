from typing import List

class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        i = 0
        while i < n:
            if nums[i] and (nums[i] <= 0 or nums[i] > n):
                nums[i] = None
                i += 1
            elif nums[i] and nums[i] == i+1:
                i += 1
            elif not nums[i]:
                i += 1
            else:
                t = nums[nums[i] - 1]
                nums[nums[i] - 1] = nums[i]
                nums[i] = t
            if i == n-1:
                break

        for idx, num in enumerate(nums):
            if not num:
                return idx+1
        return n

if __name__ == '__main__':
    sol = Solution()
    nums = [1,2,0]
    print(sol.firstMissingPositive(nums) == 3)
    nums = [3,4,-1,1]
    print(sol.firstMissingPositive(nums) == 2)
    nums = [7,8,9,11,12]
    print(sol.firstMissingPositive(nums) == 1)