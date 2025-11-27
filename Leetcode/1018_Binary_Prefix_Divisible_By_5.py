from typing import List
import pytest

class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        ans = []
        binary = ""
        for num in nums:
            binary += str(num)
            if int(binary, 2) % 5 == 0:
                ans.append(True)
            else:
                ans.append(False)
        return ans

def test_case_1():
    sol = Solution()
    nums = [0,1,1]
    actual = sol.prefixesDivBy5(nums)
    expected = [True, False, False]
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,1,1]
    actual = sol.prefixesDivBy5(nums)
    expected = [False, False, False]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()