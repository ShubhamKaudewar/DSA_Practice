import pytest
from typing import List

class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        if len(nums) == 1:
            return nums[0]

        result = []
        for i in range(len(nums) - 1):
            result.append((nums[i] + nums[i + 1]) % 10)
        return self.triangularSum(result)

def test_case_1():
    sol = Solution()
    nums = [1,2,3,4,5]
    actual = sol.triangularSum(nums)
    expected = 8
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,2,3,4,5]
    actual = sol.triangularSum(nums)
    expected = 8
    assert actual == expected

if __name__ == '__main__':
    pytest.main()