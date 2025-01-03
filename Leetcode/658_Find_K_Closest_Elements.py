from typing import List
import pytest
import bisect
import heapq

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        idx = bisect.bisect_left(arr, x)

        res = []
        right_heap = arr[idx:]
        heapq.heapify(right_heap)
        left_heap = arr[:idx]
        heapq._heapify_max(left_heap)
        while k > 0:
            if left_heap and right_heap:
                left_peek = left_heap[0]
                right_peek = right_heap[0]
                if abs(left_peek - x) <= abs(right_peek - x):
                    res.append(heapq._heappop_max(left_heap))
                else:
                    res.append(heapq.heappop(right_heap))
            elif left_heap:
                res.append(heapq._heappop_max(left_heap))
            elif right_heap:
                res.append(heapq.heappop(right_heap))
            else:
                return sorted(res)
            k -= 1
        return sorted(res)

def test_case_1():
    sol = Solution()
    assert sol.findClosestElements([1, 2, 3, 4, 5], 4, 3) == [1, 2, 3, 4]

def test_case_2():
    sol = Solution()
    assert sol.findClosestElements([1, 1, 2, 3, 4, 5], 4, -1) == [1, 1, 2, 3]

def test_case_3():
    sol = Solution()
    assert sol.findClosestElements([0,1,1,1,2,3,6,7,8,9], 9, 4) == [0,1,1,1,2,3,6,7,8]

def test_case_4():
    sol = Solution()
    assert sol.findClosestElements([0,1,2,2,2,3,6,8,8,9], 5, 9) == [3,6,8,8,9]

if __name__ == '__main__':
    pytest.main()