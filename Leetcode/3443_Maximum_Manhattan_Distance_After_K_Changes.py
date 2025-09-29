import pytest
from collections import Counter, deque

class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        

def test_case_1():
    sol = Solution()
    word = "aabcaba"
    k = 0
    expected = 3
    actual = sol.minimumDeletions(word, k)
    assert actual == expected

def test_case_2():
    sol = Solution()
    word = "dabdcbdcdcd"
    k = 2
    expected = 2
    actual = sol.minimumDeletions(word, k)
    assert actual == expected

def test_case_3():
    sol = Solution()
    word = "aaabaaa"
    k = 2
    expected = 1
    actual = sol.minimumDeletions(word, k)
    assert actual == expected

def test_case_4():
    sol = Solution()
    word = "ddknnnnnnnkddcbadcbc"
    k = 2
    expected = 5
    actual = sol.minimumDeletions(word, k)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()