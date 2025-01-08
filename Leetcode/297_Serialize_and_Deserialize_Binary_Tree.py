
import pytest
from helper import TreeNode
from typing import Optional
from collections import deque


class Codec:
    def serialize(self, root: Optional[TreeNode]) -> str:
        """Encodes a tree to a single string."""
        if not root:
            return "None"

        result = []
        queue = deque([root])

        while queue:
            node = queue.popleft()
            if node:
                result.append(str(node.val))
                queue.append(node.left)
                queue.append(node.right)
            else:
                result.append("None")

        return ",".join(result)

    def deserialize(self, data: str) -> Optional[TreeNode]:
        """Decodes your encoded data to tree."""
        if data == "None":
            return None

        nodes = data.split(",")
        root = TreeNode(int(nodes[0]))
        queue = deque([root])
        i = 1

        while queue and i < len(nodes):
            curr = queue.popleft()
            if nodes[i] != "None":
                curr.left = TreeNode(int(nodes[i]))
                queue.append(curr.left)
            i += 1

            if i < len(nodes) and nodes[i] != "None":
                curr.right = TreeNode(int(nodes[i]))
                queue.append(curr.right)
            i += 1

        return root


def test_case_1():
    ser = Codec()
    deser = Codec()
    tree = TreeNode()
    arr = [1,2,3,None,None,4,5]
    root = tree.construct_binary_tree(arr)
    expected = deser.deserialize(ser.serialize(root))
    assert tree.isIdentical(root, expected) == True

def test_case_2():
    ser = Codec()
    deser = Codec()
    tree = TreeNode()
    arr = []
    root = tree.construct_binary_tree(arr)
    expected = deser.deserialize(ser.serialize(root))
    assert tree.isIdentical(root, expected) == True


if __name__ == '__main__':
    pytest.main()