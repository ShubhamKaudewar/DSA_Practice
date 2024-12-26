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

    def merge(self, lst):
        dummy = Node(0)
        d_head = dummy
        curr1 = self.head
        curr2 = lst.head
        while curr1 and curr2:
            if curr1.value < curr2.value:
                d_head.next = curr1
                curr1 = curr1.next
            else:
                d_head.next = curr2
                curr2 = curr2.next
            d_head = d_head.next

        while curr1:
            d_head.next = curr1
            curr1 = curr1.next
            d_head = d_head.next

        while curr2:
            d_head.next = curr2
            curr2 = curr2.next
            d_head = d_head.next
        self.head = dummy.next
        temp = self.head
        new_len = 0
        while temp:
            new_len += 1
            temp = temp.next
        self.length = new_len


if __name__ == "__main__":
    l1 = LinkedList(1)
    l1.append(3)
    l1.append(5)
    l1.append(7)

    l2 = LinkedList(2)
    l2.append(4)
    l2.append(6)
    l2.append(8)

    l1.merge(l2)

    l1.print_list()