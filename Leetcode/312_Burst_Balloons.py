import pytest
from typing import List

class Solution:
    """
    The approach here is that let's have pointer L and R, in that range we will pop the idx element last,
    """
    def maxCoins(self, nums: List[int]) -> int:
        nums = [1] + nums + [1]
        cache = {}

        def dfs(l, r) -> int:
            if l > r: # out of bound
                return 0

            if (l, r) in cache:
                return cache[(l, r)]

            cache[(l, r)] = 0 # set initially 0
            for i in range(l, r+1):
                coins = nums[l-1]*nums[i]*nums[r+1] # if we have to pop i element last then we will have this comb as return value which gets added in final sum
                coins += dfs(i+1, r) + dfs(l, i-1)
                cache[(l, r)] = max(coins, cache[(l, r)])

            return cache[(l, r)]

        ans = dfs(1, len(nums)-2)
        return ans


    """Below solution if n^n"""
    def maxCoins1(self, nums: List[int]) -> int:
        cache = {}

        if len(nums) == 1:
            return nums[0]

        def dfs(sub, idx) -> int:
            if (tuple(sub), idx) in cache:
                return cache[(tuple(sub), idx)]

            if len(sub) == 1:
                return sub[0]

            for i in range(len(sub)):
                ans = dfs(sub[:i]+sub[i+1:], i)
                prev = 1 if i-1<0 else sub[i-1]
                nxt = 1 if i>len(sub)-2 else sub[i+1]
                cache[(tuple(sub), i)] = ans
                cache[tuple(sub)] = max(cache.get(tuple(sub), 0), prev*sub[i]*nxt + ans)

            return cache[tuple(sub)]

        for i in range(len(nums)):
            dfs(nums, i)
        return cache[tuple(nums)]



def test_case_1():
    sol = Solution()
    nums = [3,1,5,8]
    expected = 167
    actual = sol.maxCoins(nums)
    assert actual == expected

# def test_case_2():
#     sol = Solution()
#     nums = [1,5]
#     expected = 10
#     actual = sol.maxCoins(nums)
#     assert actual == expected
#
# def test_case_3():
#     sol = Solution()
#     nums = [9]
#     expected = 9
#     actual = sol.maxCoins(nums)
#     assert actual == expected

if __name__ == '__main__':
    pytest.main()

