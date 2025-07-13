from copy import deepcopy
import pytest

class Solution:
    def permute(self, nums):
        if not nums:
            return [[]]

        res = []
        adder = nums[0]
        child_res = self.permute(nums[1:])

        for child in child_res: #[[2,3],[3,2]]
            for i in range(len(nums)):
                child.insert(i, adder)
                res.append(deepcopy(child)) #[1,2,3], [2,1,3], [2,3,1]
                child.pop(i)
        return res


def test_case_1():
    sol = Solution()
    nums = [1,2,3]
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    actual = sol.permute(nums)
    assert actual.sort() == expected.sort()

def test_case_2():
    sol = Solution()
    nums = [0,1]
    expected = [[1,0], [0,1]]
    actual = sol.permute(nums)
    assert actual.sort() == expected.sort()

def test_case_3():
    sol = Solution()
    nums = [1]
    expected = [[1]]
    actual = sol.permute(nums)
    assert actual.sort() == expected.sort()

if __name__ == '__main__':
    pytest.main()