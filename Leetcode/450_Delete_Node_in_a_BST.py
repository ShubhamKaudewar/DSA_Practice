import pytest
from helper import TreeNode
from typing import Optional

class Solution:
    def deleteNode(self, root: Optional[TreeNode], key: int) -> Optional[TreeNode]:
        return TreeNode().delete_node(root, key)

def test_case_1():
    sol = Solution()
    tree = TreeNode()
    root = tree.construct_binary_tree([4,2,7,1,3])
    actual = sol.deleteNode(root, 3)
    expected = tree.construct_binary_tree([4,2,7,1])
    assert tree.isIdentical(actual,expected) == True

if __name__ == '__main__':
    pytest.main()