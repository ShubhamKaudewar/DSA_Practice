import pytest
from typing import List
from collections import Counter

class Solution:
    """
    This is question of greedy algo, solved using frequency map and sorted array iteration
    """
    def isNStraightHand(self, hand: List[int], groupSize: int) -> bool:
        freq_map = dict(Counter(hand))
        hand.sort()
        for n in hand:
            if freq_map.get(n):
                for mem in range(n, groupSize+n):
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
    hand = [1,2,3,6,2,3,4,7,8]
    groupSize = 3
    actual = sol.isNStraightHand(hand, groupSize)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    hand = [1,2,3,4,5]
    groupSize = 4
    actual = sol.isNStraightHand(hand, groupSize)
    expected = False
    assert actual == expected


if __name__ == '__main__':
    pytest.main()