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

    def min_value(self, curr):
        while curr.left:
            curr = curr.left
        return curr.val

    def __delete_node(self, curr, value):
        if not curr:
            return None
        if value < curr.val:
            curr.left = self.__delete_node(curr.left, value)
        elif value > curr.val:
            curr.right = self.__delete_node(curr.right, value)
        else:
            if not curr.left and not curr.right:
                return None
            elif not curr.left:
                curr = curr.right
            elif not curr.right:
                curr = curr.left
            else:
                sub_tree_min = self.min_value(curr.right)
                curr.val = sub_tree_min
                curr.right = self.__delete_node(curr.right, sub_tree_min)
        return curr

    def delete_node(self, root, value):
        return self.__delete_node(root, value)

if __name__ == '__main__':
    # Example usage
    tree = TreeNode()
    arr = [3, 9, 20, None, None, 15, 7]
    root = tree.construct_binary_tree(arr)
    print("==== END ====")