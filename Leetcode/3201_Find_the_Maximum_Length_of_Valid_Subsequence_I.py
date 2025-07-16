import pytest

class Solution:
    def maximumLength(self, nums):
        evens = sum(1 if x % 2 == 0 else 0 for x in nums)
        odds = len(nums) - evens

        def max_with_start(from_even):
            p = 0
            max_sq = 0
            check_even, check_odd = (True, False) if from_even else (False, True)
            while p < len(nums):
                if nums[p] % 2 == 0 and check_even:
                    max_sq += 1
                    check_even, check_odd = False, True
                if nums[p] % 2 == 1 and check_odd:
                    max_sq += 1
                    check_even, check_odd = True, False
                p += 1
            return max_sq

        return max(
            evens,
            odds,
            max_with_start(True),
            max_with_start(False)
        )

def test_case_1():
    sol = Solution()
    nums = [1,2,3,4]
    expected = 4
    actual = sol.maximumLength(nums)
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums = [1,2,1,1,2,1,2]
    expected = 6
    actual = sol.maximumLength(nums)
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums = [1,3]
    expected = 2
    actual = sol.maximumLength(nums)
    assert actual == expected

def test_case_4():
    sol = Solution()
    nums = [8,8,1]
    expected = 2
    actual = sol.maximumLength(nums)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()