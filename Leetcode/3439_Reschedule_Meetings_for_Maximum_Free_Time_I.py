import pytest
from typing import List

class Solution:
    def maxFreeTime(self, eventTime: int, k: int, startTime: List[int], endTime: List[int]) -> int:
        gaps = []
        gap_start = 0
        max_free_time = 0

        for i in range(len(startTime)):
            gaps.append(startTime[i] - gap_start)
            gap_start = endTime[i]
        if endTime[-1] < eventTime:
            gaps.append(eventTime - endTime[-1])

        if len(gaps) < k:
            return sum(gaps)

        curr_sum = 0
        for i in range(len(gaps)):
            curr_sum += gaps[i] - (gaps[i - (k + 1)] if i >= k + 1 else 0)
            max_free_time = max(max_free_time, curr_sum)
        return max_free_time

def test_case_1():
    sol = Solution()
    eventTime = 5
    k = 1
    startTime = [1,3]
    endTime = [2,5]
    expected = 2
    actual = sol.maxFreeTime(eventTime, k, startTime, endTime)
    assert actual == expected

def test_case_2():
    sol = Solution()
    eventTime = 10
    k = 1
    startTime = [0,2,9]
    endTime = [1,4,10]
    expected = 6
    actual = sol.maxFreeTime(eventTime, k, startTime, endTime)
    assert actual == expected

def test_case_3():
    sol = Solution()
    eventTime = 21
    k = 2
    startTime = [18,20]
    endTime = [20,21]
    expected = 18
    actual = sol.maxFreeTime(eventTime, k, startTime, endTime)
    assert actual == expected

def test_case_4():
    sol = Solution()
    eventTime = 34
    k = 2
    startTime = [0,17]
    endTime = [14,19]
    expected = 18
    actual = sol.maxFreeTime(eventTime, k, startTime, endTime)
    assert actual == expected

def test_case_5():
    sol = Solution()
    eventTime = 21
    k = 1
    startTime = [7,10,16]
    endTime = [10,14,18]
    expected = 7
    actual = sol.maxFreeTime(eventTime, k, startTime, endTime)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()