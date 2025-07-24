import pytest
from typing import List

class Solution:
    def fib(self, n: int) -> int:
        mem = [0] * (n + 1)
        if n < 2:
            return n

        def dp(n):
            if mem[n]:
                return mem[n]

            if n < 2:
                return n
            
            total = dp(n - 2) + dp(n - 1)
            mem[n] = total
            return total
        dp(n)
        return mem[n]


# def test_case_1():
#     sol = Solution()
#     n = 2
#     expected = 1
#     actual = sol.fib(n)
#     assert actual == expected

def test_case_2():
    sol = Solution()
    n = 3
    expected = 2
    actual = sol.fib(n)
    assert actual == expected

def test_case_3():
    sol = Solution()
    n = 4
    expected = 3
    actual = sol.fib(n)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()