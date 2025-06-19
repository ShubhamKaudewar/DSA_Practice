from copy import deepcopy

import pytest
from typing import List

class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        n = len(cost)
        memo = [-1] * n
        
        def dp(idx):
            if idx >= n:
                return 0
            
            if memo[idx] != -1:
                return memo[idx]

            memo[idx] = cost[idx] + min(dp(idx+1), dp(idx+2))
            return memo[idx]
            
        return min(dp(0), dp(1))


# def test_case_1():
#     sol = Solution()
#     cost = [10,15,20]
#     actual = sol.minCostClimbingStairs(cost)
#     expected = 15
#     assert actual == expected

def test_case_2():
    sol = Solution()
    cost = [1,100,1,1,1,100,1,1,100,1]
    actual = sol.minCostClimbingStairs(cost)
    expected = 6
    assert actual == expected

if __name__ == '__main__':
    pytest.main()