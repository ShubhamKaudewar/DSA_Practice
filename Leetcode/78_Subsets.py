import pytest
from typing import List

class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result = []
        subset = []
        def dp(i):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # Include idx value to subset
            subset.append(nums[i])
            dp(i+1)

            # Not include idx value to subset
            subset.pop()
            dp(i + 1)
        dp(0)
        return result


def test_case_1():
    sol = Solution()
    nums = [1,2,3]
    actual = sol.subsets(nums)
    expected = [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]
    assert set(actual) == set(expected)

if __name__ == '__main__':
    pytest.main()