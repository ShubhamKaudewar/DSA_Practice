import pytest
from helper import TreeNode
from typing import Optional

class Solution:
    def insertIntoBST(self, root: Optional[TreeNode], val: int) -> Optional[TreeNode]:
        new_node = TreeNode(val)
        if not root:
            return new_node

        def _insert(curr):
            if val < curr.val:
                if not curr.left:
                    curr.left = new_node
                    return
                _insert(curr.left)
            else:
                if not curr.right:
                    curr.right = new_node
                    return
                _insert(curr.right)
        _insert(root)
        return root


def test_case_1():
    sol = Solution()
    tree = TreeNode()
    root = tree.construct_binary_tree([4,2,7,1,3])
    actual = sol.insertIntoBST(root, 5)
    expected = tree.construct_binary_tree([4,2,7,1,3,5])
    assert tree.isIdentical(actual,expected) == True

def test_case_2():
    sol = Solution()
    tree = TreeNode()
    root = tree.construct_binary_tree([40,20,60,10,30,50,70])
    actual = sol.insertIntoBST(root, 25)
    expected = tree.construct_binary_tree([40,20,60,10,30,50,70,None,None,25])
    assert tree.isIdentical(actual,expected) == True

def test_case_3():
    sol = Solution()
    tree = TreeNode()
    root = tree.construct_binary_tree([4,2,7,1,3,None,None,None,None,None,None])
    actual = sol.insertIntoBST(root, 5)
    expected = tree.construct_binary_tree([4,2,7,1,3,5])
    assert tree.isIdentical(actual,expected) == True

if __name__ == '__main__':
    pytest.main()