from collections import deque
from typing import List
from helper import NAryTree, NAryNode

class Solution:
    def levelOrder(self, root: 'NAryNode') -> List[List[int]]:
        if not root:
            return []
        q = deque([root])
        res = []

        while q:
            level_values = []
            for _ in range(len(q)):
                curr = q.popleft()
                level_values.append(curr.val)
                for child in curr.children:
                    q.append(child)
            res.append(level_values)
        return res


if __name__ == '__main__':
    sol = Solution()
    n_arr_tree = NAryTree()
    root_array = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                  None, 14]
    root_node = n_arr_tree.buildNAryTree(root_array)
    print(sol.levelOrder(root_node))