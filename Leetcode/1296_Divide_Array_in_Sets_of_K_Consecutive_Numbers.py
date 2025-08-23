import pytest
from typing import List
from collections import Counter

class Solution:
    """
    This is question of greedy algo, solved using frequency map and sorted array iteration
    """

    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        freq_map = dict(Counter(nums))
        nums.sort()
        for n in nums:
            if freq_map.get(n):
                for mem in range(n, k+n):
                    if mem not in freq_map:
                        return False
                    freq_map[mem] -= 1
                    if freq_map[mem] == 0:
                        del freq_map[mem]
        if freq_map:
            return False
        return True

def test_case_1():
    sol = Solution()
    hand = [1,2,3,3,4,4,5,6]
    groupSize = 4
    actual = sol.isPossibleDivide(hand, groupSize)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    hand = [3,2,1,2,3,4,3,4,5,9,10,11]
    groupSize = 3
    actual = sol.isPossibleDivide(hand, groupSize)
    expected = True
    assert actual == expected

def test_case_3():
    sol = Solution()
    hand = [1,2,3,4]
    groupSize = 3
    actual = sol.isPossibleDivide(hand, groupSize)
    expected = False
    assert actual == expected


if __name__ == '__main__':
    pytest.main()