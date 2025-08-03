import pytest
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        rob1, rob2 = 0, 0

        # [rob1, rob2, n, n+1, ..]
        for n in nums:
            temp = max(rob2, n+rob1)
            rob1 = rob2
            rob2 = temp
        return rob2

def test_1():
    sol = Solution()
    nums = [1,2,3,1]
    expected = 4
    actual = sol.rob(nums)
    assert expected == actual

def test_2():
    sol = Solution()
    nums = [2,7,9,3,1]
    expected = 12
    actual = sol.rob(nums)
    assert expected == actual

def test_3():
    sol = Solution()
    nums = [2,1,1,2]
    expected = 4
    actual = sol.rob(nums)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()