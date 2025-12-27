import pytest
from typing import List
from statistics import median

class Solution:
    def maxTurbulenceSize(self, arr: List[int]) -> int:
        ans = 0
        n = len(arr)

        if min(arr) == max(arr):
            return 1

        # for everything else
        p = 1
        c = 0
        while p < n-1:
            prev, curr, nxt = arr[p-1], arr[p], arr[p+1]

            cond1 = prev > curr and curr < nxt
            cond2 = prev < curr and curr > nxt
            if cond1 or cond2:
                c += 1
            else:
                c = 0
            p += 1
            ans = max(ans, c)

        return ans+2

def test_case_1():
    sol = Solution()
    arr = [9,4,2,10,7,8,8,1,9]
    actual = sol.maxTurbulenceSize(arr)
    expected = 5
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [4,8,12,16]
    actual = sol.maxTurbulenceSize(arr)
    expected = 2
    assert actual == expected

def test_case_3():
    sol = Solution()
    arr = [100]
    actual = sol.maxTurbulenceSize(arr)
    expected = 1
    assert actual == expected

def test_case_4():
    sol = Solution()
    arr = [100, 100, 100]
    actual = sol.maxTurbulenceSize(arr)
    expected = 1
    assert actual == expected

if __name__ == '__main__':
    pytest.main()