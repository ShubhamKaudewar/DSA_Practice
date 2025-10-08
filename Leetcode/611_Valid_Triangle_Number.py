from typing import List
import pytest

class Solution:
    def triangleNumber(self, nums: List[int]) -> int:
        """Use a fixed third side (largest), and apply two pointers on the left segment to count valid pairs."""
        nums.sort()
        count = 0

        for k in range(len(nums)-1, 1, -1):
            i = 0
            j = k - 1
            while i < j:
                if nums[k] < nums[i] + nums[j]:
                    count += (j-i)
                    j -= 1
                else:
                    i += 1
        return count

def test_case_1():
    sol = Solution()
    nums = [2,2,3,4]
    actual = sol.triangleNumber(nums)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [4,2,3,4]
    actual = sol.triangleNumber(nums)
    expected = 4
    assert actual == expected

if __name__ == '__main__':
    pytest.main()