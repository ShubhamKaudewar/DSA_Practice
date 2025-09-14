import pytest
from typing import List

class Solution:
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        result = []
        nums.sort()
        used = [False] * len(nums)

        def dfs(path):
            if len(path) == len(nums):
                result.append(path[:])
                return
            for i in range(len(nums)):
                if used[i]:
                    continue
                # Since we are sorting nums then we know for sure that if previous is same then it's duplicate,
                # we can avoid that with check nums[i] == nums[i - 1]
                if i > 0 and nums[i] == nums[i - 1] and not used[i - 1]:
                    continue
                used[i] = True
                path.append(nums[i])
                dfs(path)
                path.pop()
                used[i] = False

        dfs([])
        return result


def test_case_1():
    sol = Solution()
    nums = [1,1,2]
    actual = sol.permuteUnique(nums)
    expected = [[1,1,2], [1,2,1], [2,1,1]]
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,2,3]
    actual = sol.permuteUnique(nums)
    expected = [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()