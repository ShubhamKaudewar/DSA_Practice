import pytest

class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        """
        This is typical math problem of reminder
        explained best here https://leetcode.com/problems/smallest-integer-divisible-by-k/solutions/948790/smallest-integer-divisible-by-k-by-alpeo-z9q0/?envType=daily-question&envId=2025-11-27
        """
        rem = 0
        for c in range(1, k + 1):
            rem = (rem * 10 + 1) % k
            if rem == 0:
                return c
        return -1

def test_case_1():
    sol = Solution()
    k = 1
    actual = sol.smallestRepunitDivByK(k)
    expected = 1
    assert actual == expected

def test_case_2():
    sol = Solution()
    k = 2
    actual = sol.smallestRepunitDivByK(k)
    expected = -1
    assert actual == expected

def test_case_3():
    sol = Solution()
    k = 3
    actual = sol.smallestRepunitDivByK(k)
    expected = 3
    assert actual == expected

if __name__ == '__main__':
    pytest.main()