from typing import List
import pytest

class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        n = len(gas)
        total_gas = sum(gas)
        total_cost = sum(cost)
        if total_gas < total_cost:
            return -1

        total = 0
        answer = 0
        for i in range(n):
            total += gas[i] - cost[i]
            if total < 0:
                total = 0
                answer = i + 1
        return answer if answer is not None else -1

def test_case_1():
    sol = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]
    actual = sol.canCompleteCircuit(gas, cost)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    gas = [2,3,4]
    cost = [3,4,3]
    actual = sol.canCompleteCircuit(gas, cost)
    expected = 3
    assert actual == expected

if __name__ == '__main__':
    pytest.main()