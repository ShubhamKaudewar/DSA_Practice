from typing import List, Optional, Union
from collections import deque


# Definition for a Node.
class NAryNode:
    def __init__(self, val: Optional[int] = None, children: Optional[List['NAryNode']] = None):
        self.val = val
        self.children = children if children is not None else []


class NAryTree:
    def buildNAryTree(self, root: List[Union[int, None]]) -> Optional[NAryNode]:
        if not root:
            return None

        # Initialize the root node
        root_node = NAryNode(root[0])
        queue = deque([root_node])  # Queue to track parents whose children are being added
        current_parent = queue[0]  # Current node to add children to

        # Start processing the input array from the second element
        i = 2  # `root[1]` is expected to always be `null`, so we start at index 2
        while i < len(root):
            if root[i] is None:
                # If `null` is encountered, the current parent is complete. Dequeue it.
                queue.popleft()
            else:
                # Create a new child node and add it to the current parent's children
                new_child = NAryNode(root[i])
                current_parent.children.append(new_child)
                # Add the new child to the queue for its children to be processed
                queue.append(new_child)
            i += 1

            # Update current parent
            if queue:
                current_parent = queue[0]

        return root_node


# Example usage:
if __name__ == "__main__":
    n_arr_tree = NAryTree()
    root_array = [1, None, 2, 3, 4, 5, None, None, 6, 7, None, 8, None, 9, 10, None, None, 11, None, 12, None, 13, None,
                  None, 14]
    root_node = n_arr_tree.buildNAryTree(root_array)