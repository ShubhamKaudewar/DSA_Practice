import pytest
from typing import List
import heapq

class Solution:
    def clearStars(self, s: str) -> str:
        combinations = [] #[<char>, <int>]
        output = list(s)

        for idx, c in enumerate(s):
            if c == "*":
                hc, hidx = heapq.heappop(combinations)
                output[idx] = ""
                output[-hidx] = ""
            else:
                heapq.heappush(combinations, (c, -idx))

        return "".join(output)

def test_case_1():
    sol = Solution()
    s = "aaba*"
    actual = sol.clearStars(s)
    expected = "aab"
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "abc"
    actual = sol.clearStars(s)
    expected = "abc"
    assert actual == expected

def test_case_3():
    sol = Solution()
    s = "abc*de*fgh*"
    actual = sol.clearStars(s)
    expected = "defgh"
    assert actual == expected

if __name__ == '__main__':
    pytest.main()