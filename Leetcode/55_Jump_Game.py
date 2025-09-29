from typing import List
import pytest

class Solution:
    def canJump(self, arr: List[int]) -> bool:
        if not arr or len(arr) == 1:
            return True

        result = True
        i = len(arr)-1
        steps = 0

        while i > -1:
            if arr[i] < steps:
                steps += 1
                result = False
            else:
                steps = 1
                result = True
            i -= 1
        return result

def test_case_1():
    sol = Solution()
    arr = [2,3,1,1,4]
    actual = sol.canJump(arr)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [3,2,1,0,4]
    actual = sol.canJump(arr)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()