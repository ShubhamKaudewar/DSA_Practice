import pytest


class Solution:
    def checkValidString(self, s: str) -> bool:
        left_min, left_max = 0, 0
        for c in s:
            if c == "(":
                left_min, left_max = left_min+1, left_max+1
            elif c == ")":
                # here we have choice to choose ) so decreasing min count
                left_min, left_max = max(0, left_min-1), left_max-1
            else:
                left_min, left_max = max(0, left_min-1), left_max+1

            if left_max < 0:
                return False
        return left_min == 0


def test_case_1():
    sol = Solution()
    s = "()"
    actual = sol.checkValidString(s)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "(*)"
    actual = sol.checkValidString(s)
    expected = True
    assert actual == expected

def test_case_3():
    sol = Solution()
    s = "(*))"
    actual = sol.checkValidString(s)
    expected = True
    assert actual == expected

def test_case_4():
    sol = Solution()
    s = "))(("
    actual = sol.checkValidString(s)
    expected = False
    assert actual == expected

def test_case_5():
    sol = Solution()
    s = "("
    actual = sol.checkValidString(s)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()