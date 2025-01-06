import pytest
from helper import TreeNode

class Solution:
    """
    To understand code watched this video just for intuation
    https://www.youtube.com/watch?v=WO1tfq2sbsI
    """
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root:
            return root

        def dfs(curr):
            if not curr:
                return None
            if curr.val == p.val or curr.val == q.val:
                return curr
            if not curr.left and not curr.right:
                return None

            left_val = dfs(curr.left)
            right_val = dfs(curr.right)
            if left_val and right_val:
                return curr
            elif left_val:
                return left_val
            return right_val
        return dfs(root)

    """This is more simpler version"""
    def lowestCommonAncestor1(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        if not root or root.val == p.val or root.val == q.val:
            return root

        left = self.lowestCommonAncestor(root.left, p, q)
        right = self.lowestCommonAncestor(root.right, p, q)

        return root if left and right else left or right



def test_case_1():
    sol = Solution()
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([5,6,2,None,None,7,4])
    q = tree.construct_binary_tree([1,0,8])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 3

def test_case_2():
    sol = Solution()
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([5,6,2,None,None,7,4])
    q = tree.construct_binary_tree([4])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 5

def test_case_3():
    sol = Solution()
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([2,7,4])
    q = tree.construct_binary_tree([7])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 2

def test_case_4():
    sol = Solution()
    arr = [3,5,1,6,2,0,8,None,None,7,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([5,6,2,None,None,7,4])
    q = tree.construct_binary_tree([4])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 5

def test_case_5():
    sol = Solution()
    arr = [1,2]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([1])
    q = tree.construct_binary_tree([2])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 1

def test_case_6():
    sol = Solution()
    arr = [1,2,3,None,4]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    p = tree.construct_binary_tree([4])
    q = tree.construct_binary_tree([3,None,4])
    ans_node = sol.lowestCommonAncestor(root,p, q)
    assert ans_node.val == 1

if __name__ == '__main__':
    pytest.main()