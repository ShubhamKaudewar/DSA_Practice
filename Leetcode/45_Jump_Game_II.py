from typing import List
import pytest

class Solution:
    # Better solution
    def jump(self, nums: List[int]) -> int:
        jumps = 0
        farthest = 0
        end = 0

        for i in range(len(nums) - 1):
            farthest = max(farthest, i + nums[i])
            if i == end:
                jumps += 1
                end = farthest
        return jumps


    def jump1(self, arr: List[int]) -> int:
        if not arr or len(arr) == 1:
            return 0

        result = 0
        i = len(arr) - 1
        steps = 0
        target = i
        mn = target

        while target > -1:
            steps += 1
            i -= 1
            if i < 0:
                steps = 1
                result += 1
                target = mn
                mn = 0
                i = target - 1
                if target == 0:
                    break
            if arr[i] >= steps:
                mn = i
        return result

def test_case_1():
    sol = Solution()
    arr = [2,3,1,1,4]
    actual = sol.jump(arr)
    expected = 2
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [2,3,0,1,4]
    actual = sol.jump(arr)
    expected = 2
    assert actual == expected

if __name__ == '__main__':
    pytest.main()