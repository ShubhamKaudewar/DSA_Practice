from typing import List


class Solution:
    def _merge(self, arr1, arr2):
        res = []
        i, j = 0, 0

        while i < len(arr1) and j < len(arr2):
            if arr1[i] < arr2[j]:
                res.append(arr1[i])
                i += 1
            else:
                res.append(arr2[j])
                j += 1

        while i < len(arr1):
            res.append(arr1[i])
            i += 1

        while j < len(arr2):
            res.append(arr2[j])
            j += 1

        return res

    def mergeSort(self, arr):
        if len(arr) <= 1:
            return arr
        mid = len(arr) // 2
        left = self.mergeSort(arr[:mid])
        right = self.mergeSort(arr[mid:])
        merged = self._merge(left, right)
        return merged

    def sortArray(self, nums: List[int]) -> List[int]:
        # return self.mergeSort(nums)
        return self.heapsort(nums)

    def heapsort(self, nums):
        from heapq import heapify, heappop
        heapify(nums)
        return [heappop(nums) for _ in range(len(nums))]

if __name__ == '__main__':
    sol = Solution()
    nums = [5,2,3,1]
    print(sol.sortArray(nums))