from helper import LinkedList
from typing import List
import pytest

class Solution:
    def __init__(self):
        self.ll = None

    """Detecting duplicate using slow and fast pointers"""
    def findDuplicate(self, nums: List[int]) -> int:
        slow = nums[0]
        fast = nums[0]

        # Find the meeting point of the two pointers
        while True:
            slow = nums[slow]
            fast = nums[nums[fast]]
            if slow == fast:
                break

        # Find the entrance to the cycle
        slow = nums[0]
        while slow != fast:
            slow = nums[slow]
            fast = nums[fast]

        return slow

    """Detecting duplicate using actual LL"""
    def findDuplicate1(self, nums: List[int]) -> int:
        self.ll = LinkedList(nums[0])
        self.ll.array_to_list(nums[1:])
        head = self.ll.make_cycle
        slow, fast = head, head.next
        while slow.value != fast.value:
            slow = slow.next
            fast = fast.next.next
        return slow.value

def test_case_1():
    sol = Solution()
    assert sol.findDuplicate([1,3,4,2,2]) == 2

def test_case_2():
    sol = Solution()
    assert sol.findDuplicate([3,1,3,4,2]) == 3

def test_case_3():
    sol = Solution()
    assert sol.findDuplicate([4,3,1,4,2]) == 4

if __name__ == '__main__':
    pytest.main()