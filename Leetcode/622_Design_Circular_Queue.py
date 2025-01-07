from collections import deque
import pytest


class MyCircularQueue:

    def __init__(self, k: int):
        self.dq = deque(maxlen=k)

    def enQueue(self, value: int) -> bool:
        if len(self.dq) == self.dq.maxlen:
            return False
        self.dq.append(value)
        return True

    def deQueue(self) -> bool:
        if not self.dq:
            return False
        self.dq.popleft()
        return True

    def Front(self) -> int:
        if not self.dq:
            return -1
        return self.dq[0]

    def Rear(self) -> int:
        if not self.dq:
            return -1
        return self.dq[-1]

    def isEmpty(self) -> bool:
        return len(self.dq) == 0

    def isFull(self) -> bool:
        return len(self.dq) == self.dq.maxlen

        
def test_case_1():
    mcq = None
    actions = ["MyCircularQueue", "enQueue", "enQueue", "enQueue", "enQueue", "Rear", "isFull", "deQueue", "enQueue", "Rear"]
    values = [[3], [1], [2], [3], [4], [], [], [], [4], []]
    actual = [None]
    for action, value in zip(actions, values):
        if action == "MyCircularQueue":
            mcq = MyCircularQueue(*value)
        elif action == "enQueue":
            actual.append(mcq.enQueue(*value))
        elif action == "deQueue":
            actual.append(mcq.deQueue())
        elif action == "Front":
            actual.append(mcq.Front())
        elif action == "Rear":
            actual.append(mcq.Rear())
        elif action == "isEmpty":
            actual.append(mcq.isEmpty())
        elif action == "isFull":
            actual.append(mcq.isFull())
    expected = [None, True, True, True, False, 3, True, True, True, 4]
    assert actual == expected

def test_case_2():
    mcq = None
    actions = ["MyCircularQueue","enQueue","enQueue","enQueue","enQueue","deQueue","deQueue","isEmpty","isEmpty","Rear","Rear","deQueue"]
    values = [[8],[3],[9],[5],[0],[],[],[],[],[],[],[]]
    actual = [None]
    for action, value in zip(actions, values):
        if action == "MyCircularQueue":
            mcq = MyCircularQueue(*value)
        elif action == "enQueue":
            actual.append(mcq.enQueue(*value))
        elif action == "deQueue":
            actual.append(mcq.deQueue())
        elif action == "Front":
            actual.append(mcq.Front())
        elif action == "Rear":
            actual.append(mcq.Rear())
        elif action == "isEmpty":
            actual.append(mcq.isEmpty())
        elif action == "isFull":
            actual.append(mcq.isFull())
    expected = [None,True,True,True,True,True,True,False,False,0,0,True]
    assert actual == expected

if __name__ == '__main__':
    pytest.main()