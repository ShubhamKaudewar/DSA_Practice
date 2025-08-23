import pytest
from typing import List

class Solution:
    """
    This is question of greedy, remove triple whose value of index i is grater than target index i value
    """
    def mergeTriplets(self, triplets: List[List[int]], target: List[int]) -> bool:
        value_exist_triplet = [0]*len(target)
        skip_triplet = False

        for triplet in triplets:
            for idx, val in enumerate(triplet):
                if val > target[idx]:
                    skip_triplet = True
                    break

            if not skip_triplet:
                for idx, val in enumerate(triplet):
                    if val == target[idx]:
                        value_exist_triplet[idx] = 1
            skip_triplet = False

        if sum(value_exist_triplet) == len(target):
            return True
        return False


def test_case_1():
    sol = Solution()
    triplets = [[2,5,3],[1,8,4],[1,7,5]]
    target = [2,7,5]
    actual = sol.mergeTriplets(triplets, target)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    triplets = [[3,4,5],[4,5,6]]
    target = [3,2,5]
    actual = sol.mergeTriplets(triplets, target)
    expected = False
    assert actual == expected

def test_case_3():
    sol = Solution()
    triplets = [[2,5,3],[2,3,4],[1,2,5],[5,2,3]]
    target = [5,5,5]
    actual = sol.mergeTriplets(triplets, target)
    expected = True
    assert actual == expected

def test_case_4():
    sol = Solution()
    triplets = [[3,5,1],[10,5,7]]
    target = [3,5,7]
    actual = sol.mergeTriplets(triplets, target)
    expected = False
    assert actual == expected

def test_case_5():
    sol = Solution()
    triplets = [[3,1,7],[1,5,10]]
    target = [3,5,7]
    actual = sol.mergeTriplets(triplets, target)
    expected = False
    assert actual == expected


if __name__ == '__main__':
    pytest.main()