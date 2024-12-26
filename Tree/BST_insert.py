class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


def preOrder(root):
    if root == None:
        return
    print(root.info, end=" ")
    preOrder(root.left)
    preOrder(root.right)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def __r_insert(self, current_node, value):
        if not current_node:
            current_node = Node(value)
        print(f'current_node: {current_node.info}')
        if value < current_node.info:
            current_node.left = self.__r_insert(current_node.left, value)
        if value > current_node.info:
            current_node.right = self.__r_insert(current_node.right, value)
        return current_node

    def insert(self, val):
        print(f'value received: {val}')
        if not self.root:
            self.root = Node(val)
            return
        self.__r_insert(self.root, val)

def main():
    tree = BinarySearchTree()
    arr = [4, 2, 3, 1, 7, 6]
    for i in range(len(arr)):
        tree.insert(arr[i])
    preOrder(tree.root)

if __name__ == '__main__':
    main()
