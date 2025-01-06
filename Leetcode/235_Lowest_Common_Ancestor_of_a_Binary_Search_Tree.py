import pytest
from helper import TreeNode

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root
        p, q = (p, q) if p.val <= q.val else (q, p)

        def dp(curr):
            if p.val <= curr.val <= q.val:
                return curr
            elif p.val > curr.val:
                return dp(curr.right)
            else:
                return dp(curr.left)
        return dp(root)

def test_case_1():
    sol = Solution()
    arr = [6,2,8,0,4,7,9,None,None,3,5]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([2,0,4,None,None,3,5])
    q = tree.construct_binary_tree([8,7,9])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 6

def test_case_2():
    sol = Solution()
    arr = [6,2,8,0,4,7,9,None,None,3,5]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([2,0,4,None,None,3,5])
    q = tree.construct_binary_tree([4,3,5])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 2

if __name__ == '__main__':
    pytest.main()