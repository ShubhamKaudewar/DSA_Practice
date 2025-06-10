import pytest
from helper import TreeNode
from typing import List


class Solution:
    """
    This question decision Tree is not easy to understand it is recommended to watch this video to get
    the understanding of recursion logic and understand the basecase to return
    https://youtu.be/GBKI9VSKdGg?si=wMix6mp4XJpEn4hT&t=553
    """
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        result = []
        
        def dfs(i, curr, total):
            if total == target:
                result.append(curr.copy())
                return
            
            if i >= len(candidates) or total > target:
                return
            
            curr.append(candidates[i])
            dfs(i, curr, total + candidates[i])
            curr.pop()
            dfs(i+1, curr, total)
            
        dfs(0, [], 0)
        
        return result
        
def test_case_1():
    sol = Solution()
    candidates = [2,3,6,7]
    target = 7
    expected = [[2,2,3],[7]]
    actual = sol.combinationSum(candidates, target)
    assert actual == expected

def test_case_2():
    sol = Solution()
    candidates = [2,3,5]
    target = 8
    expected = [[2,2,2,2],[2,3,3],[3,5]]
    actual = sol.combinationSum(candidates, target)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()