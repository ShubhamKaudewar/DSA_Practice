from collections import deque
from typing import List, Optional
from helper import TreeNode
import pytest

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            level_values = []
            for _ in range(len(q)):
                curr = q.popleft()
                level_values.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_values)
        return res


def test_case_1():
    sol = Solution()
    arr = [3, 9, 20, None, None, 15, 7]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    expected = [[3], [9, 20], [15, 7]]
    actual = sol.levelOrder(root)
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [1,2,3,None,5,None,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    expected = [[1], [2, 3], [5, 4]]
    actual = sol.levelOrder(root)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()