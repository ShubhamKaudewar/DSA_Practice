import pytest
from typing import Optional,List
from helper import LinkedListNode as ListNode, LinkedList

class Solution:
    def __init__(self):
        self.ll = LinkedList(0)

    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        temp = ListNode(0)
        sorting_head = temp
        for i in range(len(lists)):
            temp.next = lists[i]
            while temp.next:
                temp = temp.next

        sorted_head = self.ll.merge_sort(sorting_head.next)
        return sorted_head

def test_case_1():
    sol = Solution()
    arr = [[1,4,5],[1,3,4],[2,6]]
    lists = []
    for e in arr:
        ll = LinkedList(e[0])
        e_head = ll.array_to_list(e[1:])
        lists.append(e_head)

    exp_arr = [1,1,2,3,4,4,5,6]
    ell = LinkedList(exp_arr[0])
    exp_head = ell.array_to_list(exp_arr[1:])

    act_head = sol.mergeKLists(lists)
    assert ll.is_similar(act_head, exp_head) == True


def test_case_2():
    sol = Solution()
    arr = [[1]]
    lists = []
    for e in arr:
        ll = LinkedList(e[0])
        e_head = ll.array_to_list(e[1:])
        lists.append(e_head)

    exp_arr = [1]
    ell = LinkedList(exp_arr[0])
    exp_head = ell.array_to_list(exp_arr[1:])

    act_head = sol.mergeKLists(lists)
    assert ll.is_similar(act_head, exp_head) == True

if __name__ == '__main__':
    pytest.main()