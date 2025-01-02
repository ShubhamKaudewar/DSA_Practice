from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        candidate = 0
        count = 0
        for num in nums:
            if count == 0:
                candidate = num
                count += 1
            else:
                if candidate == num:
                    count += 1
                else:
                    count -= 1
        return candidate

if __name__ == '__main__':
    sol = Solution()
    # nums = [3,2,3]
    nums = [3,3,4]
    print(sol.majorityElement(nums))