import pytest
from typing import List
import math
from collections import Counter

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        freq_map = Counter(nums)
        n = len(nums)

        if 1 in dict(freq_map):
            return n-freq_map[1]

        min_ops = float('inf')
        for i in range(n):
            curr_gcd = nums[i]
            for j in range(i + 1, n):
                curr_gcd = math.gcd(curr_gcd, nums[j])
                if curr_gcd == 1:
                    min_ops = min(min_ops, j - i)
                    break
        if min_ops == float('inf'):
            return -1
        return min_ops + n - 1




def test_case_1():
    sol = Solution()
    nums = [2,6,3,4]
    actual = sol.minOperations(nums)
    expected = 4
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [2,10,6,14]
    actual = sol.minOperations(nums)
    expected = -1
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [1,1]
    actual = sol.minOperations(nums)
    expected = 0
    assert actual == expected

def test_case_4():
    sol = Solution()
    nums = [6,10,15]
    actual = sol.minOperations(nums)
    expected = 2
    assert actual == expected

"""
[2,10,6,14]
[2,10,6,12,14,28,280,7,21,14]
[2,10,6,12,14,28,280,7,21,14,5,35]
[2,10,6,12,14,28,280,7,21,14,35,5]
[2,10,6,12,14,28,280,21,7,14]
[6,10,15]
[4,2,1,3,6,9]
[1,1]"""
if __name__ == '__main__':
    pytest.main()