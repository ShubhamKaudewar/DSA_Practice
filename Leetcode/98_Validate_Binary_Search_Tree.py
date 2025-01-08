import pytest
from typing import Optional,List
from helper import TreeNode

class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        self.valid = True

        def isValid(curr):
            if not self.valid or (not curr.left and not curr.right):
                return [curr.val]

            left_children, right_children = [], []
            if curr.left:
                left_children = isValid(curr.left)
            if curr.right:
                right_children = isValid(curr.right)
            if (left_children and max(left_children) >= curr.val or
                right_children and min(right_children) <= curr.val):
                self.valid = False
            return [*left_children, *right_children, curr.val]
        isValid(root)
        return self.valid

def test_case_1():
    sol = Solution()
    arr = [2,1,3]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.isValidBST(root)
    expected = True
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [5,1,4,None,None,3,6]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.isValidBST(root)
    expected = False
    assert actual == expected

def test_case_3():
    sol = Solution()
    arr = [5,1,6,None,None,8,3]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.isValidBST(root)
    expected = False
    assert actual == expected

def test_case_4():
    sol = Solution()
    arr = [1,None,1]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    actual = sol.isValidBST(root)
    expected = False
    assert actual == expected

if __name__ == '__main__':
    pytest.main()