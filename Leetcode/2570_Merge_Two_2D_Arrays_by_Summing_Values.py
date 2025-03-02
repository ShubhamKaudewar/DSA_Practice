import pytest
from typing import List
from collections import defaultdict

class Solution:
    def mergeArrays(self, nums1: List[List[int]], nums2: List[List[int]]) -> List[List[int]]:
        id_val_map = defaultdict(int)
        for num in nums1: id_val_map[num[0]] += num[1]
        for num in nums2: id_val_map[num[0]] += num[1]
        result = [[k, v] for k, v in id_val_map.items()]
        result = sorted(result, key=lambda x:x[0])
        return result

def test_case_1():
    sol = Solution()
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    actual = sol.mergeArrays(nums1, nums2)
    expected = [[1,6],[2,3],[3,2],[4,6]]
    assert actual == expected

def test_case_2():
    sol = Solution()
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    actual = sol.mergeArrays(nums1, nums2)
    expected = [[1,6],[2,3],[3,2],[4,6]]
    assert actual == expected

def test_case_3():
    sol = Solution()
    nums1 = [[1,2],[2,3],[4,5]]
    nums2 = [[1,4],[3,2],[4,1]]
    actual = sol.mergeArrays(nums1, nums2)
    expected = [[1,6],[2,3],[3,2],[4,6]]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()