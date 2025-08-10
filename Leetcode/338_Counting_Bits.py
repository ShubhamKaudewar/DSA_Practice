import pytest
from typing import List

class Solution:
    """Below solution works but Time complexity of O(n) & Space complexity of O(n)
    The approach is we will be storing range values {2-3}, {4-7}, {8-15} and reusing those just by adding 1"""
    def countBits(self, n: int) -> List[int]:
        cache = {0: 0}
        ans = [0]

        b = 1
        for p in range(1, n+1):
            if p == b*2:
                b *= 2

            cache[p] = 1 + cache[p-b]
            ans.append(cache[p])
        return ans

    """Below solution works but Time complexity of O(nlogn)"""
    def countBits1(self, n: int) -> List[int]:
        output = []
        for i in range(n + 1):
            x = format(i, 'b')
            output.append(sum([int(c) for c in str(x)]))
        return output

def test_case_1():
    sol = Solution()
    n = 2
    expected = [0,1,1]
    actual = sol.countBits(n)
    assert actual == expected

def test_case_2():
    sol = Solution()
    n = 5
    expected = [0,1,1,2,1,2]
    actual = sol.countBits(n)
    assert actual == expected

def test_case_3():
    sol = Solution()
    n = 9
    expected = [0,1,1,2,1,2,2,3,1,2]
    actual = sol.countBits(n)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()