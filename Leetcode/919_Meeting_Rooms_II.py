from typing import List
import pytest
import heapq

class Interval(object):
    def __init__(self, start, end):
        self.start = start
        self.end = end

class Solution:
    def min_meeting_rooms(self, intervals: List[Interval]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x.start)
        heap = []

        for interval in intervals:
            if heap and heap[0] <= interval.start:
                heapq.heappop(heap) # schedule meeting on same day
            heapq.heappush(heap, interval.end) # schedule for new day or update time of existing same day
        return len(heap)


def test_case_1():
    sol = Solution()
    intervals = [Interval(*x) for x in [(0,30),(5,10),(15,20)]]
    expected = 2
    actual = sol.min_meeting_rooms(intervals)
    assert actual == expected

def test_case_2():
    sol = Solution()
    intervals = [Interval(*x) for x in [(2,7)]]
    expected = 1
    actual = sol.min_meeting_rooms(intervals)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()
