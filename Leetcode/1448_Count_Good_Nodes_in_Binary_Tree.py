import pytest
from typing import Optional,List
from helper import TreeNode

class Solution:
    def goodNodes(self, root: TreeNode) -> int:
        self.good = 0
        path = []
        def dfs(curr):
            path.append(curr.val)
            if curr.val == max(path):
                self.good += 1
            if not curr.left and not curr.right:
                return

            if curr.left:
                dfs(curr.left)
                path.pop()
            if curr.right:
                dfs(curr.right)
                path.pop()
        dfs(root)
        return self.good

def test_case_1():
    sol = Solution()
    arr = [3,1,4,3,None,1,5]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.goodNodes(root)
    expected = 4
    assert actual == expected

if __name__ == '__main__':
    pytest.main()