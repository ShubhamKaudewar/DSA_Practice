from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        k = nums[0]
        left, right = 0, len(nums) - 1

        if nums[left] < nums[right]:
            return nums[left]

        while left < right:
            mid = (left + right) // 2
            if nums[mid] < k:
                right = mid
            else:
                left = mid + 1
        return nums[left]

if __name__ == '__main__':
    sol = Solution()
    # nums = [3,4,5,1,2]
    # print(sol.findMin(nums))
    # nums = [4,5,6,7,0,1,2]
    # print(sol.findMin(nums))
    nums = [11,13,15,17]
    print(sol.findMin(nums))