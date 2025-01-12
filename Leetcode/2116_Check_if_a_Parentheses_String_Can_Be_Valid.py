import pytest


class Solution:
    def canBeValid(self, s: str, locked: str) -> bool:
        n = len(s)
        if n%2 == 1: return False

        balance_left, balance_right = 0, 0
        for i in range(n):
            if locked[i] == "0" or s[i] == "(": balance_left += 1
            else: balance_left -= 1
            if balance_left < 0: return False

            if locked[n-(i+1)] == "0" or s[n-(i+1)] == ")": balance_right -= 1
            else: balance_right += 1
            if balance_right > 0: return False
        return True

def test_case_1():
    sol = Solution()
    s = "))()))"
    locked = "010100"
    actual = sol.canBeValid(s, locked)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "()()"
    locked = "0000"
    actual = sol.canBeValid(s, locked)
    expected = True
    assert actual == expected

def test_case_3():
    sol = Solution()
    s = ")"
    locked = "0"
    actual = sol.canBeValid(s, locked)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()