from typing import List
import pytest

class Solution:
    def combinationSum2(self, candidates: List[int], target: int) -> List[List[int]]:
        res = []
        candidates.sort() #[1,1,2,5,6,7,10]
        n = len(candidates)

        def backtrack(start, arr, total):
            if total == target:
                res.append(arr[:])
            if total > target:
                return

            prev = -1
            for i in range(start, n):
                if candidates[i] == prev:
                    continue
                arr.append(candidates[i])
                backtrack(i+1, arr, total+candidates[i])
                arr.pop()
                prev = candidates[i]

        backtrack( 0, [], 0)
        return res


def test_case_1():
    sol = Solution()
    candidates = [10,1,2,7,6,1,5]
    target = 8
    expected = [
        [1,1,6],
        [1,2,5],
        [1,7],
        [2,6]
    ]
    actual = sol.combinationSum2(candidates, target)
    assert actual == expected

def test_case_2():
    sol = Solution()
    candidates = [2,5,2,1,2]
    target = 5
    expected = [
        [1,2,2],
        [5]
    ]
    actual = sol.combinationSum2(candidates, target)
    assert actual == expected
    
if __name__ == '__main__':
    pytest.main()