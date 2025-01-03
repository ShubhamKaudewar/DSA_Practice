from collections import deque
from typing import List, Optional
from helper import TreeNode

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            level_values = []
            for _ in range(len(q)):
                curr = q.popleft()
                level_values.append(curr.val)
                if curr.left:
                    q.append(curr.left)
                if curr.right:
                    q.append(curr.right)
            res.append(level_values)
        return res


if __name__ == '__main__':
    sol = Solution()
    arr = [3, 9, 20, None, None, 15, 7]
    tree = TreeNode()
    root = tree.construct_binary_tree(arr)
    print(sol.levelOrder(root))