import pytest
from typing import List

class Solution:
    def isPrefixAndSuffix(self, word1: str, word2: str) -> bool:
        l = len(word1)
        if word2[:l] == word2[-l:] == word1:
            return True
        return False

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        pairs = 0
        for i in range(len(words)-1):
            for j in range(i+1, len(words)):
                if words[i] > words[j]:
                    continue
                pairs += 1 if self.isPrefixAndSuffix(words[i], words[j]) else 0
        return pairs

def test_case_1():
    sol = Solution()
    words = ["a","aba","ababa","aa"]
    expected = 4
    actual = sol.countPrefixSuffixPairs(words)
    assert actual == expected

# def test_case_2():
#     sol = Solution()
#     words = ["a","aba","ababa","aa"]
#     expected = 4
#     actual = sol.countPrefixSuffixPairs(words)
#     assert actual == expected

if __name__ == '__main__':
    pytest.main()