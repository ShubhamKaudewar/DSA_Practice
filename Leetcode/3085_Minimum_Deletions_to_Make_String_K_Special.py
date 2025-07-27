import pytest
from collections import Counter, deque

class Solution:
    """
    This gif shows the algorithm logic
    https://assets.leetcode.com/users/images/54bba303-2d66-4324-8408-e0117a3f4722_1750485191.153973.gif
    """
    def minimumDeletions(self, word: str, k: int) -> int:
        freq = dict(Counter(word))
        freqs = sorted(freq.values())

        result = float('inf')
        for idx_i, freq in enumerate(freqs):
            limit = freq + k
            removed = 0

            for idx_j, f in enumerate(freqs):
                if idx_i == idx_j:
                    continue

                if f < freq:
                    removed += f
                elif f > limit:
                    removed += f - limit
            result = min(result, removed)

        return result

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