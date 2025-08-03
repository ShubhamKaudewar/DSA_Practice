import pytest
from typing import List

class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        output = []
        for num in nums:
            output.append(int(str(num)[::-1]))
        nums.extend(output)
        result = len(set(nums))
        return result

def test_1():
    sol = Solution()
    nums = [1,13,10,12,31]
    expected = 6
    actual = sol.countDistinctIntegers(nums)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()