import pytest
from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        s = 0
        p = 0
        max_sum = float('-inf')
        cur_sum = 0
        uniques = set()
        n = len(nums)

        while s < n and p < n:
            if nums[p] in uniques:
                max_sum = max(max_sum, cur_sum)
                while True:
                    uniques.discard(nums[s])
                    cur_sum -= nums[s]
                    if nums[s] == nums[p]:
                        s += 1
                        break
                    s += 1
            else:
                uniques.add(nums[p])
                cur_sum += nums[p]
                p += 1

        return max(max_sum, cur_sum)

def test_case_1():
    sol = Solution()
    nums = [1,4,2,4,5,6]
    expected = 17
    actual = sol.maximumUniqueSubarray(nums)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [5,2,1,2,5,2,1,2,5]
    expected = 8
    actual = sol.maximumUniqueSubarray(nums)
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [10000,1,10000,1,1,1,1,1,1]
    expected = 10001
    actual = sol.maximumUniqueSubarray(nums)
    assert actual == expected

def test_case_4():
    sol = Solution()
    nums = [4078,1065,3781,6541,304,9192,5474,3049,6281,385,1531,3194,7445,9453,6210,5165,6203,9272,6798,1719,6618,1580,3353,2387,5477,2289,8431,2653,6842,481,5777,4494,5935,7983,8983,9216,6897,3467,4598,6343,6429,7830,9543,1312,5491,5748,8252,4271,2345,1358,3924,741,1844,5695,322,3204,3815,1432,9226,3372,6007,3916,9402,5363,7240,9291,9821,3543,7215,3691,3149,5295,7813,3049,710,6500,4893,7063,4647,6865,7190,2844,7508,6811,7719,2916,3496,9861,5385,5655]
    expected = 428472
    actual = sol.maximumUniqueSubarray(nums)
    assert actual == expected

def test_case_5():
    sol = Solution()
    nums = [1,2,3,4,5]
    expected = 15
    actual = sol.maximumUniqueSubarray(nums)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()