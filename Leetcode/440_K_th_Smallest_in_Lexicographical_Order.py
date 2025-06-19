import pytest
from typing import List

class Solution:
    """
    This neetcode explaining the O(logN) approach to solve using dfs 
    https://www.youtube.com/watch?v=wRubz1zhVqk
    """
    def findKthNumber(self, n: int, k: int) -> int: # n: 1341 k: 400
        curr = 1
        i = 1
        
        def count(curr):
            res = 0 # Result to count steps (elegant way)
            nei = curr + 1 # For 1 neighbour is 2 with whom level we will be comparing
            while curr <= n: # 1 <= 1341 || 100 <= 1341 || 1000 <= 1341
                nei = min(nei, n+1) # nei is min (1342, 2000) It will be 2, 20, 200 & 1342 (not 2000)
                res += nei - curr # Difference is 2 - 1 || 20 - 10 so 1 || 10 steps to add to result
                curr *= 10
                nei *= 10
            return res
            
        while i < k:
            steps = count(curr)
            if i + steps <= k: 
                curr += 1 # Moving right is step of one 1 -> 2 || 11 -> 12
                i += steps # To move right need steps
            else:
                curr *= 10 # Moving bottom is factor of 10 1 -> 10 -> 100
                i += 1 # To move bottom need one step 
        return curr

def test_case_1():
    sol = Solution()
    n = 13
    k = 2
    actual = sol.findKthNumber(n, k)
    expected = 10
    assert actual == expected

def test_case_2():
    sol = Solution()
    n = 1
    k = 1
    actual = sol.findKthNumber(n, k)
    expected = 1
    assert actual == expected


if __name__ == '__main__':
    pytest.main()