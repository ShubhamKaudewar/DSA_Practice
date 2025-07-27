import pytest
import heapq

class MedianFinder:

    def __init__(self):
        self.high = []  # to store lower values
        self.low = []  # to store higher values

    def addNum(self, num: int) -> None:
        heapq.heappush(self.low, -num)
        heapq.heappush(self.high, -heapq.heappop(self.low))

        if len(self.high) > len(self.low):
            heapq.heappush(self.low, -heapq.heappop(self.high))

    def findMedian(self) -> float:
        if len(self.low) > len(self.high):
            return -self.low[0]
        else:
            return (-self.low[0]+self.high[0]) / 2

def test_case_1():
    medianFinder = MedianFinder()
    commands = ["MedianFinder", "addNum", "addNum", "findMedian", "addNum", "findMedian"]
    values = [[], [1], [2], [], [3], []]

    response = []
    for command, value in zip(commands, values):
        if command == "MedianFinder":
            medianFinder = MedianFinder()
            response.append(None)
        elif command == "addNum":
            medianFinder.addNum(*value)
            response.append(None)
        elif command == "findMedian":
            response.append(medianFinder.findMedian())

    expected = [None, None, None, 1.5, None, 2.0]
    assert response == expected

if __name__ == '__main__':
    pytest.main()