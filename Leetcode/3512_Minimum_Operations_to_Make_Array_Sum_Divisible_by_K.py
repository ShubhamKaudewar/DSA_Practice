from typing import List
import pytest

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        return sum(nums) % k

def test_case_1():
    sol = Solution()
    nums = [3,9,7]
    k = 5
    actual = sol.minOperations(nums, k)
    expected = 4
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [4,1,3]
    k = 4
    actual = sol.minOperations(nums, k)
    expected = 0
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [3,2]
    k = 6
    actual = sol.minOperations(nums, k)
    expected = 5
    assert actual == expected

if __name__ == '__main__':
    pytest.main()