import pytest
from typing import Optional,List

class Solution:
    def maxBottlesDrunk(self, numBottles: int, numExchange: int) -> int:
        full_bottles = numBottles
        empty_bottles = 0
        drunk_bottles = 0

        while full_bottles > 0 or empty_bottles >= numExchange:
            if empty_bottles >= numExchange:
                full_bottles += 1
                empty_bottles -= numExchange
                numExchange += 1
            else:
                empty_bottles += full_bottles
                drunk_bottles += full_bottles
                full_bottles = 0
        return drunk_bottles

def test_case_1():
    sol = Solution()
    numBottles = 13
    numExchange = 6
    actual = sol.maxBottlesDrunk(numBottles, numExchange)
    expected = 15
    assert actual == expected

def test_case_2():
    sol = Solution()
    numBottles = 10
    numExchange = 3
    actual = sol.maxBottlesDrunk(numBottles, numExchange)
    expected = 13
    assert actual == expected

if __name__ == '__main__':
    pytest.main()