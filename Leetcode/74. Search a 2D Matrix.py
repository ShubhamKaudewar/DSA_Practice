from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        def bs(nums, start, end):
            if start > end:
                return -1
            mid = start + (end - start) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                return bs(nums, mid + 1, end)
            elif nums[mid] > target:
                return bs(nums, 0, mid - 1)

        def bsm(start, end):
            if start > end:
                return -1
            mid = start + (end - start) // 2

            if matrix[mid][0] <= target <= matrix[mid][-1]:
                return bs(matrix[mid], 0, len(matrix[0]) - 1)
            elif target > matrix[mid][-1]:
                return bsm(mid + 1, end)
            elif target < matrix[mid][0]:
                return bsm(0, mid - 1)
        final = bsm(0, len(matrix) - 1)
        return False if final == -1 else True

if __name__ == '__main__':
    sol = Solution()
    # matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    # target = 3
    matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]]
    target = 13
    print(sol.searchMatrix(matrix, target))