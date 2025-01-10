import pytest
from typing import List
from collections import Counter

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        """
        1. Example: If `words2 = ["lo", "eo"]`, the frequency map for each word is:
            - `"lo"` → `{l: 1, o: 1}`
            - `"eo"` → `{e: 1, o: 1}`

        The "max frequency" map will be:
            - `{l: 1, e: 1, o: 1}`

        Using this, you'll only need to compare `words1` against this single
        "max frequency" map instead of each individual word in `words2`.
        """
        max_freq_map = {}
        for word in words2:
            for char, count in Counter(word).items():
                max_freq_map[char] = max(max_freq_map.get(char, 0), count)

        output = []
        for word in words1:
            is_universal = True
            max_freq_map1 = Counter(word)
            for char, count in max_freq_map.items():
                if max_freq_map1[char] < count:
                    is_universal = False
                    break
            if is_universal: output.append(word)
        return output

def test_case_1():
    sol = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","o"]
    actual = sol.wordSubsets(words1, words2)
    expected = ["facebook","google","leetcode"]
    assert actual == expected

def test_case_2():
    sol = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["e","oo"]
    actual = sol.wordSubsets(words1, words2)
    expected = ["facebook","google"]
    assert actual == expected

def test_case_3():
    sol = Solution()
    words1 = ["amazon","apple","facebook","google","leetcode"]
    words2 = ["lo","eo"]
    actual = sol.wordSubsets(words1, words2)
    expected = ["google","leetcode"]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()