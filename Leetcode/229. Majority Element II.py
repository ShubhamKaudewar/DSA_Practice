from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        t_hold = len(nums) / 3
        freq_map = dict(Counter(nums))
        result = [k for k,v in freq_map.items() if v > t_hold]
        return result

if __name__ == '__main__':
    sol = Solution()
    nums = [3,2,3]
    print(sol.majorityElement(nums))
    nums = [1]
    print(sol.majorityElement(nums))
    nums = [1,2]
    print(sol.majorityElement(nums))