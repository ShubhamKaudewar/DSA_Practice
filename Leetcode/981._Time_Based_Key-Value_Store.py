from typing import List
from collections import defaultdict
class TimeMap:
    def __init__(self):
        self.store = defaultdict(list)

    def set(self, key: str, value: str, timestamp: int) -> None:
        self.store[key].append([value, timestamp])

    def get(self, key: str, timestamp: int) -> str:
        res = ""
        values = self.store.get(key, [])
        left, right = 0, len(values) - 1
        while left <= right:
            mid = (left + right) // 2
            if values[mid][1] <= timestamp:
                res = values[mid][0]
                left = mid + 1
            else:
                right = mid - 1
        return res

if __name__ == '__main__':
    obj = TimeMap()
    obj.set(*["foo", "bar", 1])
    print("bar" == obj.get(*["foo", 1]))
    print("bar" == obj.get(*["foo", 3]))
    obj.set(*["foo", "bar2", 4])
    print("bar2" == obj.get(*["foo", 4]))
    print("bar2" == obj.get(*["foo", 5]))
