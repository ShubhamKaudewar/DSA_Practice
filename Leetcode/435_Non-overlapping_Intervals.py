from typing import List
import pytest

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Sort intervals by end time instead of start
        intervals.sort(key=lambda x: x[1])
        ans = 0
        prev_end = float('-inf')

        for start, end in intervals:
            if start < prev_end:
                # Overlap detected, increment removal count
                ans += 1
            else:
                # No overlap, update the end marker
                prev_end = end

        return ans

    """
    The below logic work but it is not much efficient code and logic
    """
    def eraseOverlapIntervals1(self, intervals: List[List[int]]) -> int:
        intervals.sort()
        ans = 0

        k = 0
        while k < len(intervals) - 1:
            if intervals[k + 1][0] < intervals[k][-1] <= max(intervals[k + 1][-1], intervals[k][-1]):
                if k < len(intervals)-2 and intervals[k][-1] > intervals[k+2][0]:
                    if intervals[k+1][-1] > intervals[k+2][0] and intervals[k+1][-1] > intervals[k][-1]:
                        del intervals[k+1]
                    else:
                        del intervals[k]
                else:
                    del intervals[k + 1]
                ans += 1
            else:
                k += 1
        return ans

def test_case_1():
    sol = Solution()
    intervals = [[1,2],[2,3],[3,4],[1,3]]
    expected = 1
    actual = sol.eraseOverlapIntervals(intervals)
    assert actual == expected

def test_case_2():
    sol = Solution()
    intervals = [[1,2],[1,2],[1,2]]
    expected = 2
    actual = sol.eraseOverlapIntervals(intervals)
    assert actual == expected

def test_case_3():
    sol = Solution()
    intervals = [[1,2],[2,3]]
    expected = 0
    actual = sol.eraseOverlapIntervals(intervals)
    assert actual == expected

def test_case_4():
    sol = Solution()
    intervals = [[1,100],[11,22],[1,11],[2,12]]
    expected = 2
    actual = sol.eraseOverlapIntervals(intervals)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()
