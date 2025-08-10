import pytest

class Solution:
    """ return the sum of the two integers without using the operators + and -
    This is problem of bit manipulations, solved using XOR + AND with << (bit shift left by 1)
    Masks we have to use for negative integer
    Python's built-in int type does not distinguish between signed and unsigned integers in the same way that languages like C do. Python integers are arbitrarily precise, meaning they can represent numbers of any size, limited only by available memory"""
    def getSum(self, a: int, b: int) -> int:
        mask = 0xffffffff
        while b & mask != 0:
            a, b = a ^ b, (a & b) << 1
        return a & mask if b > mask else a


def test_case_1():
    sol = Solution()
    a = 1
    b = 2
    expected = 3
    actual = sol.getSum(a, b)
    assert actual == expected

def test_case_2():
    sol = Solution()
    a = 2
    b = 3
    expected = 5
    actual = sol.getSum(a, b)
    assert actual == expected

def test_case_3():
    sol = Solution()
    a = 9
    b = 11
    expected = 20
    actual = sol.getSum(a, b)
    assert actual == expected

def test_case_4():
    sol = Solution()
    a = -1
    b = 1
    expected = 0
    actual = sol.getSum(a, b)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()