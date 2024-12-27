from typing import List

class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        def merge(array1, array2):
            combined = []
            i = 0
            j = 0
            while i < len(array1) and j < len(array2):
                if array1[i] < array2[j]:
                    combined.append(array1[i])
                    i += 1
                else:
                    combined.append(array2[j])
                    j += 1

            while i < len(array1):
                combined.append(array1[i])
                i += 1

            while j < len(array2):
                combined.append(array2[j])
                j += 1

            return combined

        def merge_sort(lst):
            if len(lst) == 1:
                return lst
            mid_index = len(lst) // 2
            left_lst = merge_sort(lst[:mid_index])
            right_lst = merge_sort(lst[mid_index:])
            return merge(left_lst, right_lst)

        sorted_arr = merge_sort(nums1+nums2)
        mid = len(sorted_arr)//2
        res = sorted_arr[mid]
        if len(sorted_arr) % 2 == 0:
            res = (sorted_arr[mid] + sorted_arr[mid-1])/2
        return res

if __name__ == '__main__':
    sol = Solution()
    nums1 = [1, 3]
    nums2 = [2, 4]
    print(sol.findMedianSortedArrays(nums1, nums2))
