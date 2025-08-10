import pytest
from typing import List

class Solution:
    """This question has multiple answers"""
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)
        res = n
        for i in range(n):
            res += i - nums[i]
        return res

    def missingNumber2(self, nums: List[int]) -> int:
        n = len(nums)
        xorr = n
        for i in range(n):
            xorr ^= nums[i] ^ i
        return xorr

    def missingNumber1(self, nums: List[int]) -> int:
        present = set(nums)
        ideal = set([x for x in range(len(nums)+1)])
        missing = ideal - present
        return list(missing)[0]

def test_case_1():
    sol = Solution()
    nums = [3,0,1]
    expected = 2
    actual = sol.missingNumber(nums)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [0,1]
    expected = 2
    actual = sol.missingNumber(nums)
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [9,6,4,2,3,5,7,0,1]
    expected = 8
    actual = sol.missingNumber(nums)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()