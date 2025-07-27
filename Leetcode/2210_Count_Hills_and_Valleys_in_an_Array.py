import pytest
from typing import List
from helper.Trie import Trie

class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        c = 1
        p = 2
        n = len(nums)
        total = 0

        while c < n-1 and p < n:
            back = nums[c-1]
            front = nums[p]
            curr = nums[c]

            if front == curr:
                p += 1
                continue


            if (curr > back and curr > front) or (curr < back and curr < front):
                total += 1
            c = p
            p = c+1

        return total

def test_case_1():
    sol = Solution()
    nums = [2, 4, 1, 1, 6, 5]
    expected = 3
    actual = sol.countHillValley(nums)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [6,6,5,5,4,1]
    expected = 0
    actual = sol.countHillValley(nums)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()