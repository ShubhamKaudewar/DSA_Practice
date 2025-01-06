
import pytest
'''
# Intuition
The problem can be solved using binary search techniques by dividing it into three parts: finding the peak of the mountain, searching in the ascending part, and searching in the descending part. This ensures efficiency by utilizing the sorted nature of both halves of the array.

# Approach
1. Find the peak index of the mountain array using binary search. This is the point where an element is greater than its neighbors.
2. Perform a binary search on the left (ascending) part of the array to find the target.
3. If the target is not found, perform a binary search on the right (descending) part of the array.
4. Use caching to minimize calls to `MountainArray.get()`.

# Complexity
- Time complexity:
$$O(\log(n))$$ for peak finding + $$O(\log(n))$$ for left and right searches = $$O(\log(n))$$ overall.

- Space complexity:
$$O(n)$$ for caching the accessed elements to minimize calls.

# Code
'''

class MountainArray:
    def __init__(self, array):
        self.array = array

    def get(self, index: int) -> int:
        return self.array[index]

    def length(self) -> int:
        return len(self.array)

class Solution:
    def __init__(self):
        self.cache = {}
        self.ma = None

    def call(self, index: int) -> int:
        if index not in self.cache:
            self.cache[index] = self.ma.get(index)
        return self.cache[index]

    def findInMountainArray(self, target: int, ma: MountainArray) -> int:
        self.ma = ma

        # Step 1: Find the peak index
        left, right = 0, ma.length() - 1
        while left < right:
            mid = (left + right) // 2
            if self.call(mid) < self.call(mid + 1):  # Ascending
                left = mid + 1
            else:  # Descending or peak
                right = mid
        peak_idx = left

        # Step 2: Search in the ascending part (0 to peak_idx)
        left, right = 0, peak_idx
        while left <= right:
            mid = (left + right) // 2
            if self.call(mid) == target:
                return mid
            elif self.call(mid) < target:
                left = mid + 1
            else:
                right = mid - 1

        # Step 3: Search in the descending part (peak_idx to end)
        left, right = peak_idx, ma.length() - 1
        while left <= right:
            mid = (left + right) // 2
            if self.call(mid) == target:
                return mid
            elif self.call(mid) > target:
                left = mid + 1
            else:
                right = mid - 1

        return -1


def test_case_1():
    sol = Solution()
    arr = [1,2,3,4,5,3,1]
    ma = MountainArray(arr)
    assert sol.findInMountainArray(3, ma) == 2

def test_case_2():
    sol = Solution()
    arr = [0,1,2,4,2,1]
    ma = MountainArray(arr)
    assert sol.findInMountainArray(3, ma) == -1

def test_case_3():
    sol = Solution()
    arr = [0,5,3,1]
    ma = MountainArray(arr)
    assert sol.findInMountainArray(1, ma) == 3

if __name__ == '__main__':
    pytest.main()