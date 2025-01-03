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
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            if i == n-1:
                break

        for idx, num in enumerate(nums):
            if not num:
                return idx+1
        return n

    """
    Time Complexity: O(n)
    This is more optimized use cyclic sort and index swap. 
    This code will pass 1 edge case for which above code failing as TLE
    """
    def firstMissingPositive2(self, nums: List[int]) -> int:
        n = len(nums)

        for i in range(n):
            # Place nums[i] in its correct position if possible
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with nums[nums[i] - 1]
                nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]

        # Find the first index where the number is not in the correct position
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1

        # If all numbers are in the correct position, return n + 1
        return n + 1

if __name__ == '__main__':
    sol = Solution()
    # nums = [1,2,0]
    # print(sol.firstMissingPositive2(nums) == 3)
    nums = [3,4,-1,1]
    print(sol.firstMissingPositive2(nums) == 2)
    nums = [7,8,9,11,12]
    print(sol.firstMissingPositive2(nums) == 1)