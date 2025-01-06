class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

    def insert_level_order(self, arr, root, i, n):
        if i < n:
            temp = TreeNode(arr[i]) if arr[i] is not None else None
            root = temp

            if temp is not None:
                root.left = self.insert_level_order(arr, root.left, 2 * i + 1, n)
                root.right = self.insert_level_order(arr, root.right, 2 * i + 2, n)
        return root

    def construct_binary_tree(self, arr):
        return self.insert_level_order(arr, None, 0, len(arr))

    def isIdentical(self, curr, subCurr):
        if not curr and not subCurr:
            return True
        if not curr or not subCurr:
            return False
        return (curr.val == subCurr.val and
                self.isIdentical(curr.left, subCurr.left) and
                self.isIdentical(curr.right, subCurr.right))


if __name__ == '__main__':
    # Example usage
    tree = TreeNode()
    arr = [3, 9, 20, None, None, 15, 7]
    root = tree.construct_binary_tree(arr)
    print("==== END ====")