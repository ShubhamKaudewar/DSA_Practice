import pytest
from heapq import heappop, heappush
from typing import List

class Solution:
    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        i = 0
        attended = 0
        day = 0
        min_heap = []
        n = len(events)

        while i < n or min_heap:
            if not min_heap:
                day = events[i][0]

            while i < n and events[i][0] <= day:
                heappush(min_heap, events[i][1])
                i += 1

            while min_heap and min_heap[0] < day:
                heappop(min_heap)

            if min_heap:
                heappop(min_heap)
                attended += 1
            day += 1
        return attended

def test_case_1():
    sol = Solution()
    events = [[1,2],[2,3],[3,4]]
    expected = 3
    actual = sol.maxEvents(events)
    assert actual == expected


def test_case_2():
    sol = Solution()
    events = [[1,2],[2,3],[3,4],[1,2]]
    expected = 4
    actual = sol.maxEvents(events)
    assert actual == expected


def test_case_3():
    sol = Solution()
    events = [[1,2],[1,2],[3,3],[1,5],[1,5]]
    expected = 5
    actual = sol.maxEvents(events)
    assert actual == expected


# def test_case_4():
#     sol = Solution()
#     events = [[1,2],[2,3],[3,4]]
#     expected = 3
#     actual = sol.maxEvents(events)
#     assert actual == expected



if __name__ == '__main__':
    pytest.main()