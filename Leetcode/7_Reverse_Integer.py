import pytest

class Solution:
    def reverse(self, x: int) -> int:
        if x > 0:
            rev = int(str(x)[::-1])
        else:
            rev = -1*int(str(-1*x)[::-1])
        if -2**31 <= rev < 2**31:
            return rev
        return 0


def test_case_1():
    sol = Solution()
    x = 123
    expected = 321
    actual = sol.reverse(x)
    assert actual == expected

def test_case_2():
    sol = Solution()
    x = -123
    expected = -321
    actual = sol.reverse(x)
    assert actual == expected

def test_case_3():
    sol = Solution()
    x = 120
    expected = 21
    actual = sol.reverse(x)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()