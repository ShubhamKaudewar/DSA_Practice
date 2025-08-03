import pytest
from typing import List

class Solution:
    def rob(self, nums: List[int]) -> int:
        """
        applying from left to right gives the same result as right to left.
        apply house robber I on nums(1,n-1)
        apply house robber I on nums(2, n)
        return max(answer obtained in step 1, answer obtained in step 2)
        This is sufficient.
        """
        if not nums:
            return 0
        if len(nums) == 1:
            return nums[0]
        if len(nums) == 2:
            return max(nums)

        rob1, rob2 = 0, 0
        for n in nums[:-1]:
            temp = max(rob2, n+rob1)
            rob1 = rob2
            rob2 = temp
        path_1 = rob2

        rob1, rob2 = 0, 0
        for n in reversed(nums[1:]):
            temp = max(rob2, n+rob1)
            rob1 = rob2
            rob2 = temp
        path_2 = rob2

        return max(path_1, path_2)

def test_1():
    sol = Solution()
    nums = [2,3,2]
    expected = 3
    actual = sol.rob(nums)
    assert expected == actual

def test_2():
    sol = Solution()
    nums = [1,2,3,1]
    expected = 4
    actual = sol.rob(nums)
    assert expected == actual

def test_3():
    sol = Solution()
    nums = [1,2,3]
    expected = 3
    actual = sol.rob(nums)
    assert expected == actual

def test_4():
    sol = Solution()
    nums = [1, 2, 3, 4, 5, 1, 2, 3, 4, 5]
    expected = 16
    actual = sol.rob(nums)
    assert expected == actual

def test_5():
    sol = Solution()
    nums = [1]
    expected = 1
    actual = sol.rob(nums)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()