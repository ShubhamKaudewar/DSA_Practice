from typing import List
import pytest

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Solution 1"""
        n = len(nums)
        leftProd = [1]*n
        rightProd = [1]*n

        for i in range(1, n):
            leftProd[i] = nums[i-1] * leftProd[i-1]
            rightProd[n-i-1] = nums[n-i] * rightProd[n-i]

        ans = []
        for i in range(n):
            ans.append(leftProd[i] * rightProd[i])
        return ans

    def productExceptSelf2(self, nums):
        """Solution 2"""
        n = len(nums)
        result = [1] * n

        # Calculate prefix products
        prefix = 1
        for i in range(n):
            result[i] = prefix
            prefix *= nums[i]

        # Calculate suffix products and multiply with prefix products
        suffix = 1
        for i in range(n - 1, -1, -1):
            result[i] *= suffix
            suffix *= nums[i]

        return result




def test_case_1():
    sol = Solution()
    nums = [1, 2, 3, 4]
    actual = sol.productExceptSelf(nums)
    expected = [24,12,8,6]
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [-1,1,0,-3,3]
    actual = sol.productExceptSelf(nums)
    expected = [0,0,9,0,0]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()