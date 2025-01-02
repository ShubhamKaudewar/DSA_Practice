from typing import List

class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        """
        Here we are checking the count of the candidate number. Only for 1 possible solution for to be
        majority element. Which is frequency of the candidate number > n/2
        In majority element II problem, we are checking frequency of all the numbers > n/2. Which are possible
        solution are 2 candidates. So we will initialize two candidates here
        """
        candidate1, candidate2 = None, None
        count1, count2 = 0, 0
        for num in nums:
            if count1 == 0 and candidate2 != num:
                candidate1 = num
                count1 = 1
            elif count2 == 0 and candidate1 != num:
                candidate2 = num
                count2 = 1
            elif candidate1 == num: count1 += 1
            elif candidate2 == num:count2 += 1
            else: count1 -= 1; count2 -= 1

        count1, count2 = 0, 0
        for num in nums:
            if num == candidate1: count1 += 1
            elif num == candidate2: count2 += 1
        res = []
        if count1 >= (len(nums) // 3) + 1:
            res.append(candidate1)
        if count2 >= (len(nums) // 3) + 1:
            res.append(candidate2)
        return sorted(res)

    # This solution also works
    def majorityElement2(self, nums: List[int]) -> List[int]:
        from collections import Counter
        t_hold = len(nums) / 3
        freq_map = dict(Counter(nums))
        result = [k for k,v in freq_map.items() if v > t_hold]
        return result

if __name__ == '__main__':
    sol = Solution()
    # nums = [3,2,3]
    # print(sol.majorityElement(nums))
    # nums = [1]
    # print(sol.majorityElement(nums))
    # nums = [1,2]
    # print(sol.majorityElement(nums))
    nums = [2,1,1,3,1,4,5,6]
    print(sol.majorityElement(nums))