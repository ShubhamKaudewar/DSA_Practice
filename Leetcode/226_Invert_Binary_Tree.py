from helper.BinaryTree import TreeNode
from typing import Optional
import pytest

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        if not root:
            return root
        root.left, root.right = root.right, root.left
        self.invertTree(root.left)
        self.invertTree(root.right)
        return root


def test_case_1():
    sol = Solution()
    tree = TreeNode()
    arr = [4,2,7,1,3,6,9]
    invertedArr = [4,7,2,9,6,3,1]
    root = tree.construct_binary_tree(arr)
    actual = sol.invertTree(root)
    expected = tree.construct_binary_tree(invertedArr)
    assert True == tree.isIdentical(actual, expected)

def test_case_2():
    sol = Solution()
    tree = TreeNode()
    arr = [2,1,3]
    invertedArr = [2,3,1]
    root = tree.construct_binary_tree(arr)
    actual = sol.invertTree(root)
    expected = tree.construct_binary_tree(invertedArr)
    assert True == tree.isIdentical(actual, expected)

if __name__ == '__main__':
    pytest.main()