from typing import List
import pytest
from collections import defaultdict

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        """This is reminder tracking game need to watch video for better and detailed explanation
        Video: https://www.youtube.com/watch?v=bcXy-T4Sc3E
        """
        count = defaultdict(int)
        count[0] = 1
        ans = 0
        prefSum = 0

        for num in nums:
            prefSum += num
            rem = prefSum % k

            if rem in count:
                ans += count[rem]
            count[rem] += 1
        return ans

    # [4,5,0,-2,-3,1]
    def subarraysDivByK1(self, nums: List[int], k: int) -> int:
        """This has for loop which is O(n^2) and gives TLE"""
        prefixSum, suffixSum = [0], [0]
        n = len(nums)
        ans = 0
        total_sum = sum(nums)

        for i in range(n):
            prefixSum.append(prefixSum[-1] + nums[i])
            suffixSum.insert(0, suffixSum[0] + nums[n-i-1])

        for i in range(n):
            for j in range(i, n):
                total = total_sum - prefixSum[i] - suffixSum[j+1]
                if total % k == 0:
                    ans += 1

        return ans



def test_case_1():
    sol = Solution()
    nums = [4,5,0,-2,-3,1]
    k = 5
    actual = sol.subarraysDivByK(nums, k)
    expected = 7
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [5]
    k = 9
    actual = sol.subarraysDivByK(nums, k)
    expected = 0
    assert actual == expected


if __name__ == '__main__':
    pytest.main()