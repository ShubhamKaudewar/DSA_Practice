import pytest
from typing import List

class Solution:
    def largestPerimeter(self, nums: List[int]) -> int:
        nums.sort()
        n = len(nums)
        ans = 0

        for i in range(n-1, 1, -1):
            if nums[i] < nums[i-1] + nums[i-2]:
                ans = nums[i] + nums[i-1] + nums[i-2]
                return ans
        return ans

def test_case_1():
    sol = Solution()
    nums = [2,1,2]
    actual = sol.largestPerimeter(nums)
    expected = 5
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,2,1,10]
    actual = sol.largestPerimeter(nums)
    expected = 0
    assert actual == expected

if __name__ == '__main__':
    pytest.main()