import pytest
from typing import Optional
from helper import TreeNode

class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def isIdentical(curr, subCurr):
            if not curr and not subCurr:
                return True
            if not curr or not subCurr:
                return False
            return (curr.val == subCurr.val and
                isIdentical(curr.left, subCurr.left) and
                isIdentical(curr.right, subCurr.right))

        # Check for None cases
        if not root:
            return False  # If root is None, subtree can't exist
        if not subRoot:
            return True # An empty tree is a subtree of any tree

        return (isIdentical(root, subRoot) or
                self.isSubtree(root.left, subRoot) or
                self.isSubtree(root.right, subRoot))



# def test_case_1():
#     sol = Solution()
#     tree = TreeNode()
#     root = tree.construct_binary_tree([3,4,5,1,2])
#     subRoot = tree.construct_binary_tree([4,1,2])
#     assert sol.isSubtree(root, subRoot) == True

# def test_case_2():
#     sol = Solution()
#     tree = TreeNode()
#     root = tree.construct_binary_tree([3,4,5,1,2,None,None,None,None,0])
#     subRoot = tree.construct_binary_tree([4,1,2])
#     assert sol.isSubtree(root, subRoot) == False

def test_case_3():
    sol = Solution()
    tree = TreeNode()
    root = tree.construct_binary_tree([1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,None,1,2])
    subRoot = tree.construct_binary_tree([1,None,1,None,1,None,1,None,1,None,1,2])
    assert sol.isSubtree(root, subRoot) == True

if __name__ == '__main__':
    pytest.main()