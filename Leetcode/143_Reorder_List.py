import pytest
from typing import Optional
from helper import LinkedListNode, LinkedList

class Solution:
    def __init__(self):
        self.ll = LinkedList(0)

    def reorderList(self, head: Optional[LinkedListNode]) -> None:
        if not head or not head.next:
            return head
        start = head

        while start.next and start.next.next:
            pivot = start
            while pivot.next.next:
                pivot = pivot.next
            nxt = start.next # store ref of 2
            start.next = pivot.next # bing 1 -> 9
            start.next.next = nxt # bind 9 -> 2
            pivot.next = None # bind 8 -> None
            start = nxt # move start => 2

def test_case_1():
    sol = Solution()
    arr = [1,2,3,4,5,6,7,8,9]
    ll = LinkedList(arr[0])
    act_head = ll.array_to_list(arr[1:])

    exp_arr = [1,9,2,8,3,7,4,6,5]
    ell = LinkedList(exp_arr[0])
    exp_head = ell.array_to_list(exp_arr[1:])

    sol.reorderList(act_head)
    assert ll.is_similar(act_head, exp_head) == True

def test_case_2():
    sol = Solution()
    arr = [1,2,3,4]
    ll = LinkedList(arr[0])
    act_head = ll.array_to_list(arr[1:])

    exp_arr = [1,4,2,3]
    ell = LinkedList(exp_arr[0])
    exp_head = ell.array_to_list(exp_arr[1:])

    sol.reorderList(act_head)
    assert ll.is_similar(act_head, exp_head) == True

if __name__ == '__main__':
    pytest.main()