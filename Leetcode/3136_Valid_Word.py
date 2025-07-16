import pytest

class Solution:
    def isValid(self, word):
        if len(word) < 3: #It contains a minimum of 3 characters.
            return False

        one_vowel = False
        one_consonant = False

        for ch in word:
            if ch.isalpha():
                if ch.lower() in 'aeiou':
                    one_vowel = True
                else:
                    one_consonant = True
            elif ch.isnumeric():
                continue
            else:
                return False

        if one_vowel and one_consonant:
            return True
        return False

def test_case_1():
    sol = Solution()
    word = "234Adas"
    expected = True
    actual = sol.isValid(word)
    assert actual == expected

def test_case_2():
    sol = Solution()
    word = "b3"
    expected = False
    actual = sol.isValid(word)
    assert actual == expected

def test_case_3():
    sol = Solution()
    word = "a3$e"
    expected = False
    actual = sol.isValid(word)
    assert actual == expected

def test_case_4():
    sol = Solution()
    word = "UuE6"
    expected = False
    actual = sol.isValid(word)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()