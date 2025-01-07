import pytest
from typing import Optional, List
from helper import TreeNode
from collections import deque

class Solution:
    """Directly using this from 102_Binary_Tree_Level_Order_Traversal"""
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

    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        if not root:
            return []

        level_values = self.levelOrder(root)
        for level in level_values:
            res.append(level[-1])
        return res

def test_case_1():
    sol = Solution()
    arr = [3, 9, 20, None, None, 15, 7]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    expected = [3, 20, 7]
    actual = sol.rightSideView(root)
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [1,2,3,None,5,None,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    expected = [1, 3, 4]
    actual = sol.rightSideView(root)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()