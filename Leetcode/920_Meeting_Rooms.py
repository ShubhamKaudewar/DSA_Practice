from typing import List
import pytest
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def canAttendMeetings(self, intervals: List[Interval]) -> bool:
        if not intervals:
            return True

        start = []
        end = []
        heapq.heappush(start, intervals[0].start)
        heapq.heappush(end, intervals[0].end)

        for interval in intervals[1:]:
            if interval.start < end[-1] and interval.end > start[-1]:
                return False
            heapq.heappush(start, interval.start)
            heapq.heappush(end, interval.end)
        return True


def test_case_1():
    sol = Solution()
    intervals = [Interval(*x) for x in [(0,30),(5,10),(15,20)]]
    expected = False
    actual = sol.canAttendMeetings(intervals)
    assert actual == expected

def test_case_2():
    sol = Solution()
    intervals = [Interval(*x) for x in [(5,8),(9,15)]]
    expected = True
    actual = sol.canAttendMeetings(intervals)
    assert actual == expected

def test_case_3():
    sol = Solution()
    intervals = [Interval(*x) for x in []]
    expected = True
    actual = sol.canAttendMeetings(intervals)
    assert actual == expected

def test_case_4():
    sol = Solution()
    intervals = [Interval(*x) for x in [(5,10),(0,4)]]
    expected = True
    actual = sol.canAttendMeetings(intervals)
    assert actual == expected



if __name__ == '__main__':
    pytest.main()
