import pytest
from typing import Optional
from helper import TreeNode

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        if not root:
            return True
        self.balanced = True

        def getHeight(curr):
            if not curr: return 0
            if not curr.left and not curr.right: return 1

            lh = getHeight(curr.left)
            rh = getHeight(curr.right)
            if abs(lh - rh) > 1:
                self.balanced = False
                return 0
            return max(lh, rh) + 1
        getHeight(root)
        return self.balanced

# def test_case_1():
#     sol = Solution()
#     arr = [3,9,20,None,None,15,7]
#     tree = TreeNode()
#     root = tree.construct_binary_tree(arr)
#     assert sol.isBalanced(root) == True

# def test_case_2():
#     sol = Solution()
#     arr = [1,2,2,3,3,None,None,4,4]
#     tree = TreeNode()
#     root = tree.construct_binary_tree(arr)
#     assert sol.isBalanced(root) == False

def test_case_3():
    sol = Solution()
    arr = [1,2]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    assert sol.isBalanced(root) == True

if __name__ == '__main__':
    pytest.main()