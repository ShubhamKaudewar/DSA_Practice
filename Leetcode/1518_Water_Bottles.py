import pytest
from typing import Optional,List

class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        drank = numBottles
        while numBottles >= numExchange:
            new = numBottles // numExchange
            numBottles = new + numBottles % numExchange
            drank += new
        return drank

def test_case_1():
    sol = Solution()
    numBottles = 9
    numExchange = 3
    actual = sol.numWaterBottles(numBottles, numExchange)
    expected = 13
    assert actual == expected

def test_case_2():
    sol = Solution()
    numBottles = 15
    numExchange = 4
    actual = sol.numWaterBottles(numBottles, numExchange)
    expected = 19
    assert actual == expected

if __name__ == '__main__':
    pytest.main()