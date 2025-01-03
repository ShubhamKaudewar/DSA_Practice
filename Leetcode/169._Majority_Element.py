from typing import List
from collections import Counter

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Here we are checking the count of the candidate number. Only for 1 possible solution for to be
        majority element. Which is frequency of the candidate number > n/2
        In majority element II problem, we are checking frequency of all the numbers > n/2. Which are possible
        solution are 2 candidates. So we will initialize two candidates there
        """
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