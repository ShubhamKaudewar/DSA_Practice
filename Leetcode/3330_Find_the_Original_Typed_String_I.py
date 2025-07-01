import pytest


class Solution:
    def possibleStringCount(self, word: str) -> int:
        result = 1
        for i in range(len(word)-1):
            if word[i] == word[i+1]:
                result += 1
        return result



def test_case_1():
    sol = Solution()
    word = "abbcccc"
    expected = 5
    actual = sol.possibleStringCount(word)
    assert actual == expected

def test_case_2():
    sol = Solution()
    word = "abcd"
    expected = 1
    actual = sol.possibleStringCount(word)
    assert actual == expected

def test_case_3():
    sol = Solution()
    word = "aaaa"
    expected = 4
    actual = sol.possibleStringCount(word)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()