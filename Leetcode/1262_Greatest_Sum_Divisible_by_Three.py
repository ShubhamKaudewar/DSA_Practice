from typing import List
import pytest

class Solution:
    def maxSumDivThree(self, nums: List[int]) -> int:
        """
        If remainder = 1 → you need to remove either one smallest element with remainder 1, or two smallest elements with remainder 2.
        If remainder = 2 → you need to remove either one smallest element with remainder 2, or two smallest elements with remainder 1.
        """
        nums.sort()
        total_sum = sum(nums)
        rem = total_sum % 3
        if rem == 1:
            sum1, sum2 = 0, 0
            for num in nums:
                if num % 3 == 1:
                    sum1 = total_sum - num
                    break

            c, tmp = 0, 0
            for num in nums:
                if c == 2: break
                if num % 3 == 2:
                    sum2 = total_sum - num - tmp
                    tmp = num
                    c += 1

            if c < 1:
                if sum1 == 0:
                    return 0
                else:
                    return sum1
            return max(sum1, sum2)
        elif rem == 2:
            sum1, sum2 = 0, 0
            for num in nums:
                if num % 3 == 2:
                    sum1 = total_sum - num
                    break

            c, tmp = 0, 0
            for num in nums:
                if c == 2: break
                if num % 3 == 1:
                    sum2 = total_sum - num - tmp
                    tmp = num
                    c += 1

            if c < 2:
                if sum1 == 0:
                    return 0
                else:
                    return sum1
            return max(sum1, sum2)
        return total_sum

def test_case_1():
    sol = Solution()
    nums = [3,6,5,1,8]
    actual = sol.maxSumDivThree(nums)
    expected = 18
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [4]
    actual = sol.maxSumDivThree(nums)
    expected = 0
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [1,2,3,4,4]
    actual = sol.maxSumDivThree(nums)
    expected = 12
    assert actual == expected

def test_case_4():
    sol = Solution()
    nums = [2,6,2,2,7]
    actual = sol.maxSumDivThree(nums)
    expected = 15
    assert actual == expected

def test_case_5():
    sol = Solution()
    nums = [3,1,2]
    actual = sol.maxSumDivThree(nums)
    expected = 6
    assert actual == expected

def test_case_6():
    sol = Solution()
    nums = [9,6,61]
    actual = sol.maxSumDivThree(nums)
    expected = 15
    assert actual == expected

if __name__ == '__main__':
    pytest.main()