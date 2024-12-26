class Node:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
    
    def print_list(self):
        if not self.head:
            print("Empty list")
            return
            
        current = self.head
        while current:
            print(current.value, end=" <-> ")
            current = current.next
        print("None")

dll = DoublyLinkedList(7)
dll = DoublyLinkedList(17)
dll = DoublyLinkedList(1)
dll = DoublyLinkedList(9)
dll.print_list()

