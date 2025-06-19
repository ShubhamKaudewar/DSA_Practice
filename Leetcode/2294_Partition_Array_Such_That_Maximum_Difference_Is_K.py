import pytest
from typing import List

class Solution:
    def partitionArray(self, nums: List[int], k: int) -> int:
        nums.sort()
        n = len(nums)
        result = 0
        i, p = 0, 1

        while p <= n:
            if p == n:
                result += 1
                break

            if nums[p] - nums[i] > k:
                result += 1
                i = p
            p += 1
        return result

def test_case_1():
    sol = Solution()
    nums = [3,6,1,2,5]
    k = 2
    expected = 2
    actual = sol.partitionArray(nums, k)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,2,3]
    k = 1
    expected = 2
    actual = sol.partitionArray(nums, k)
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [2,2,4,5]
    k = 0
    expected = 3
    actual = sol.partitionArray(nums, k)
    assert actual == expected

def test_case_4():
    sol = Solution()
    nums = [0]
    k = 0
    expected = 1
    actual = sol.partitionArray(nums, k)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()