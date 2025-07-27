from typing import List
import pytest

class Solution:
    def merge(self, i: List[List[int]]) -> List[List[int]]:
        i.sort()
        k = 0
        while k<len(i)-1:
            if i[k+1][0] <= i[k][-1] <= max(i[k+1][-1], i[k][-1]):
                new_i = [i[k][0], max(i[k+1][-1], i[k][-1])]
                del i[k+1]
                del i[k]
                i.append(new_i)
                i.sort()
            else:
                k += 1
        return i


def test_case_1():
    sol = Solution()
    intervals = [[1,3],[2,6],[8,10],[15,18]]
    expected = [[1,6],[8,10],[15,18]]
    actual = sol.merge(intervals)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()
