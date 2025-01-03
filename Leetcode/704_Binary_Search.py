from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:

        def bs(start, end):
            if start > end:
                return -1
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(mid + 1, end)
            elif nums[mid] > target:
                return bs(0, mid - 1)
        return bs(0, len(nums) - 1)

sol = Solution()
nums = [-1,0,3,5,9,12]
target = 9
# nums = [-1,0,3,5,9,12]
# target = 2
print(sol.search(nums, target))