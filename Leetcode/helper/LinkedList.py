
class LinkedListNode:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        new_node = LinkedListNode(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    @staticmethod
    def is_similar(head_one, head_two):
        while head_one is not None and head_two is not None:
            if head_one.value != head_two.value:
                return False
            head_one = head_one.next
            head_two = head_two.next
        return head_one is None and head_two is None
    
    @staticmethod
    def calculate_length(head):
        length = 0
        while head is not None:
            length += 1
            head = head.next
        return length

    @staticmethod
    def merge_sort(head):
        # Base case: if the list is empty or has only one node, it's already sorted
        if not head or not head.next:
            return head

        def split_list(head):
            """Splits the linked list into two halves."""
            slow, fast = head, head.next
            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            middle = slow.next
            slow.next = None
            return head, middle

        def merge_sorted_lists(left, right):
            """Merges two sorted linked lists into one sorted list."""
            dummy = LinkedListNode(0)
            tail = dummy
            while left and right:
                if left.value < right.value:
                    tail.next, left = left, left.next
                else:
                    tail.next, right = right, right.next
                tail = tail.next
            tail.next = left or right  # Attach the remaining nodes
            return dummy.next

        # Step 1: Split the list into two halves
        left_half, right_half = split_list(head)

        # Step 2: Recursively sort each half
        left_sorted = LinkedList.merge_sort(left_half)
        right_sorted = LinkedList.merge_sort(right_half)

        # Step 3: Merge the sorted halves
        return merge_sorted_lists(left_sorted, right_sorted)

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next
    
    
    
    def append(self, value):
        new_node = LinkedListNode(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1
    
    def print_list_from_head(self, head):
        temp = head
        while temp is not None:
            print(temp.value, end="")
            temp = temp.next
            if temp.next:
                print("->", end="")

    def insertion_sort(self):
        if self.length < 2:
            return
        dummy = LinkedListNode(0)
        d_tail = dummy
        while self.head:
            det = self.head
            # print(f'detached node: {det.value}')
            self.head = self.head.next
            # if self.head:
                # print(f'head set to: {self.head.value}')
            temp = dummy
            prev = temp
            # print(f'set temp and next to: {temp.value}')
            is_less = False
            while temp:
                # print(f'comparing new node {temp.value} to detached {det.value}')
                if temp.value > det.value:
                    det.next = temp
                    prev.next = det
                    # print(f'new node is {prev.next.value} -> {prev.next.next.value}')
                    is_less = True
                    break
                prev = temp
                temp = temp.next
            if not is_less:
                det.next = None
                d_tail.next = det
                d_tail = d_tail.next
                # print(f'insert at tail** new node tail is {d_tail.value}')

        # setting head and tails
        self.head = dummy.next
        temp = self.head
        while temp.next:
            temp = temp.next
        self.tail = temp
        return self.head


    def array_to_list(self, arr):
        for e in arr:
            self.append(e)
        return self.head

    @property
    def make_cycle(self):
        self.tail.next = self.head
        return self.head
    
    
    
class DoublyLinkedNode:
    def __init__(self, value):
        self.value = value
        self.next = None
        self.prev = None


class DoublyLinkedList:
    def __init__(self, value):
        new_node = DoublyLinkedNode(value)
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