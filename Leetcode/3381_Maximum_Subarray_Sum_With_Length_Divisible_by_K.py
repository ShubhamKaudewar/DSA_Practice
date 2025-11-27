from typing import List
import pytest

class Solution:
    def maxSubarraySum(self, nums: List[int], k: int) -> int:
        pref = [0]

        for num in nums:
            pref.append(pref[-1]+num)

        ans = float('-inf')
        # store minimum prefix sum for each index remainder class
        min_pref = [float('inf')] * k
        min_pref[0] = 0  # base case: empty prefix

        for j in range(1, len(pref)):  # skip pref[0] since it's the base
            mod = j % k

            # candidate subarray sum
            ans = max(ans, pref[j] - min_pref[mod])

            # update minimum prefix for this remainder class
            min_pref[mod] = min(min_pref[mod], pref[j])
        return ans

def test_case_1():
    sol = Solution()
    nums = [1,2]
    k = 1
    actual = sol.maxSubarraySum(nums, k)
    expected = 3
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [-1,-2,-3,-4,-5]
    k = 4
    actual = sol.maxSubarraySum(nums, k)
    expected = -10
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [-5,1,2,-3,4]
    k = 2
    actual = sol.maxSubarraySum(nums, k)
    expected = 4
    assert actual == expected

if __name__ == '__main__':
    pytest.main()