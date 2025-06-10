from copy import deepcopy

import pytest
from typing import List
from collections import Counter


class Solution:
    def maxDifference(self, s: str) -> int:
        max_odd = 0
        min_even = 101
        
        freq_map = Counter(s)
        
        for c, f in freq_map.items():
            if f % 2 == 1:
                max_odd = max(max_odd, f)
            else:
                min_even = min(min_even, f)
        return max_odd - min_even

def test_case_1():
    sol = Solution()
    s = "aaaaabbc"
    actual = sol.maxDifference(s)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "abcabcab"
    actual = sol.maxDifference(s)
    expected = 1
    assert actual == expected


if __name__ == '__main__':
    pytest.main()