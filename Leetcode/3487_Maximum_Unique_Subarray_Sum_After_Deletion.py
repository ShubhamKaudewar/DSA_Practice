import pytest
from typing import List

class Solution:
    def maxSum(self, nums: List[int]) -> int:
        uniques = set(x for x in nums if x>0)
        if not len(uniques):
            return max(nums) # all negative return minimum negative value
        return sum(uniques)

def test_case_1():
    sol = Solution()
    nums = [1,2,3,4,5]
    expected = 15
    actual = sol.maxSum(nums)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,1,0,1,1]
    expected = 1
    actual = sol.maxSum(nums)
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [1,2,-1,-2,1,0,-1]
    expected = 3
    actual = sol.maxSum(nums)
    assert actual == expected

def test_case_4():
    sol = Solution()
    nums = [-17,-15]
    expected = -15
    actual = sol.maxSum(nums)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()