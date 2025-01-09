
import pytest
from typing import List
import re

class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        total = 0

        """Using startswith"""
        for word in words:
            if word.startswith(pref): total += 1

        """Using regex match pattern"""
        # for word in words:
        #     present = re.match(rf'^{pref}', word)
        #     if present: total += 1
        return total

        """One liner solution"""
        # return sum(1 for w in words if w.startswith(pref))

def test_case_1():
    sol = Solution()
    words = ["pay","attention","practice","attend"]
    pref = "at"
    actual = sol.prefixCount(words, pref)
    expected = 2
    assert actual == expected

def test_case_2():
    sol = Solution()
    words = ["leetcode","win","loops","success"]
    pref = "code"
    actual = sol.prefixCount(words, pref)
    expected = 0
    assert actual == expected


if __name__ == '__main__':
    pytest.main()