import pytest
from typing import Optional,List
from helper import TreeNode

class Solution:
    def kthSmallest(self, root: Optional[TreeNode], k: int) -> int:
        smallest = []
        def dfs(curr):
            nonlocal smallest

            if not curr.left and not curr.right:
                smallest.append(curr.val)
                return

            # check left
            if curr.left:
                dfs(curr.left)
            if len(smallest) >= k:
                return

            # check middle
            smallest.append(curr.val)
            if len(smallest) >= k:
                return

            # check right
            if curr.right:
                dfs(curr.right)
            if len(smallest) >= k:
                return
        dfs(root)
        return smallest[k-1]

def test_case_1():
    sol = Solution()
    arr, k = [3,1,4,None,2], 1
    expected = 1
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.kthSmallest(root, k)
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr, k = [5,3,6,2,4,None,None,1], 3
    expected = 3
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.kthSmallest(root, k)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()