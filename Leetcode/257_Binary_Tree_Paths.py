import pytest
from helper import TreeNode
from typing import List, Optional


class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        result = []
        
        def dfs(curr, children: List[int]):
            children.append(curr.val)

            if curr.left:
                dfs(curr.left, children)
                children.pop()

            if curr.right:
                dfs(curr.right, children)
                children.pop()
            
            if not curr.left and not curr.right:
                result.append("->".join(map(str, children)))

        dfs(root, [])
        return result


def test_case_1():
    sol = Solution()
    arr = [1,2,3,None,5]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    expected = ["1->2->5","1->3"]
    actual = sol.binaryTreePaths(root)
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [1]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    expected = ["1"]
    actual = sol.binaryTreePaths(root)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()