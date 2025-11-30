from typing import List
import pytest
from collections import defaultdict

class Solution:
    def minSubarray(self, nums: List[int], p: int) -> int:
        total = sum(nums)
        target = total % p

        if target == 0:
            return 0

        count = defaultdict(int)
        count[0] = -1
        ans = len(nums)
        prefSum = 0

        for i, num in enumerate(nums):
            prefSum = (prefSum + num) % p
            needed = (prefSum - target + p) % p

            if needed in count:
                ans = min(ans, i - count[needed])
            count[prefSum] = i

        return ans if ans < len(nums) else -1

def test_case_1():
    sol = Solution()
    nums = [3,1,4,2]
    p = 6
    actual = sol.minSubarray(nums, p)
    expected = 1
    assert actual == expected


if __name__ == '__main__':
    pytest.main()