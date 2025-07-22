from copy import deepcopy

import pytest

class Solution:
    def subsetsWithDup(self, nums):
        """
        This question is of backtracking neetcode 150
        :param nums:
        :return:
        """
        output = []
        if len(nums) == 0:
            return [[]]

        adder = nums[0]
        res = self.subsetsWithDup(nums[1:])
        output.extend(deepcopy(res))
        for x in deepcopy(res):
            x.append(adder)
            x.sort()
            if x not in output:
                output.append(x)
        output.sort()
        return output

def test_case_1():
    sol = Solution()
    nums = [1,2,2]
    expected = [[],[1],[1,2],[1,2,2],[2],[2,2]]
    actual = sol.subsetsWithDup(nums)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [0]
    expected = [[],[0]]
    actual = sol.subsetsWithDup(nums)
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [4,4,4,1,4]
    expected = [[],[1],[1,4],[1,4,4],[1,4,4,4],[1,4,4,4,4],[4],[4,4],[4,4,4],[4,4,4,4]]
    actual = sol.subsetsWithDup(nums)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()