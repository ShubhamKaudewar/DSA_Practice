import pytest
from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        if not nums:
            return 0

        lis = []
        for num in nums:
            pos = bisect_left(lis, num)
            if pos == len(lis):
                lis.append(num) # this append higher value at end of list
            else:
                lis[pos] = num # this replace min value at that position with greater value

        return len(lis)


def test_1():
    sol = Solution()
    nums = [10,9,2,5,3,7,101,18]
    expected = 4
    actual = sol.lengthOfLIS(nums)
    assert expected == actual

def test_2():
    sol = Solution()
    nums = [0,1,0,3,2,3]
    expected = 4
    actual = sol.lengthOfLIS(nums)
    assert expected == actual

def test_3():
    sol = Solution()
    nums = [7,7,7,7,7,7,7]
    expected = 1
    actual = sol.lengthOfLIS(nums)
    assert expected == actual


if __name__ == "__main__":
    pytest.main()