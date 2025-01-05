from typing import List
import pytest


class Solution:
    def search(self, nums: List[int], target: int) -> int:
        return target in set(nums)

def test_case_1():
    sol = Solution()
    assert sol.search([2,5,6,0,0,1,2], 0) == True

def test_case_2():
    sol = Solution()
    assert sol.search([2,5,6,0,0,1,2], 3) == False

def test_case_3():
    sol = Solution()
    assert sol.search([1,1,1,1,1,1,1,1,1,1,1,1,1,2,1,1,1,1,1], 2) == True

if __name__ == '__main__':
    pytest.main()