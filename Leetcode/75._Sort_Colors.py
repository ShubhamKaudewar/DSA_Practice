from typing import List
from collections import Counter

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        i, r = 0, 0
        while i < len(nums):
            if nums[i] == 0:
                nums.pop(i)
                nums.insert(0, 0)
                i += 1
                r = 0
            elif nums[i] == 2 and r < len(nums) - i:
                nums.pop(i)
                nums.append(2)
                r += 1
            else:
                i += 1
                r = 0
        return nums

if __name__ == '__main__':
    sol = Solution()
    nums = [2,0,2,1,1,0]
    print(sol.sortColors(nums))