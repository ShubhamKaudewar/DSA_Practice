import collections
from typing import List
import pytest

class Solution:
    def countPalindromicSubsequence(self, s: str) -> int:
        left = set()
        right = collections.Counter(s)
        result = set()

        for middle in range(len(s)):
            right[s[middle]] -= 1
            if right[s[middle]] == 0:
                right.pop(s[middle])

            for j in range(26):
                char = chr(ord("a") + j)
                if char in right and char in left:
                    result.add((s[middle], char))
            left.add(s[middle])
        return len(result)

def test_case_1():
    sol = Solution()
    assert sol.countPalindromicSubsequence("aabca") == 3

def test_case_2():
    sol = Solution()
    assert sol.countPalindromicSubsequence("adc") == 0

def test_case_3():
    sol = Solution()
    assert sol.countPalindromicSubsequence("bbcbaba") == 4

if __name__ == '__main__':
    pytest.main()