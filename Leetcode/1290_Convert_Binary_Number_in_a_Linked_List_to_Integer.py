import pytest
from helper import LinkedListNode, LinkedList

class Solution:
    def getDecimalValue(self, head: LinkedListNode) -> int:
        if not head.next:
            return head.value

        curr = head
        binary_str = ""
        while curr:
            binary_str += str(curr.value)
            curr = curr.next
        return int(binary_str, 2)


def test_case_1():
    sol = Solution()
    arr = [1,0,1]
    ll = LinkedList(arr[0])
    act_head = ll.array_to_list(arr[1:])
    expected = 5
    actual = sol.getDecimalValue(act_head)
    assert actual == expected

def test_case_2():
    sol = Solution()
    arr = [0]
    ll = LinkedList(arr[0])
    act_head = ll.array_to_list(arr[1:])
    expected = 0
    actual = sol.getDecimalValue(act_head)
    assert actual == expected

def test_case_3():
    sol = Solution()
    arr = [1]
    ll = LinkedList(arr[0])
    act_head = ll.array_to_list(arr[1:])
    expected = 1
    actual = sol.getDecimalValue(act_head)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()