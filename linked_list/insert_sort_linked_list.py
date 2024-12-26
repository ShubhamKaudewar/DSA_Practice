class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        new_node = Node(value)
        self.head = new_node
        self.tail = new_node
        self.length = 1

    def print_list(self):
        temp = self.head
        while temp is not None:
            print(temp.value)
            temp = temp.next

    def append(self, value):
        new_node = Node(value)
        if self.head is None:
            self.head = new_node
            self.tail = new_node
        else:
            self.tail.next = new_node
            self.tail = new_node
        self.length += 1

    def insertion_sort(self):
        if self.length < 2:
            return
        dummy = Node(0)
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

if __name__ == "__main__":
    my_linked_list = LinkedList(4)
    my_linked_list.append(2)
    my_linked_list.append(5)
    my_linked_list.append(1)
    my_linked_list.append(3)
    my_linked_list.append(6)

    print("Linked List Before Sort:")
    my_linked_list.print_list()

    my_linked_list.insertion_sort()

    print("\nSorted Linked List:")
    my_linked_list.print_list()
