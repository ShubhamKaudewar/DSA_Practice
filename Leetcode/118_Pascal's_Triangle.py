from typing import List

class Solution:
    def __generate(self, arr):
        result = [arr[0]]
        for i in range(len(arr)-1):
            result.append(arr[i]+arr[i+1])
        result.append(arr[-1])
        return result


    def generate(self, n: int) -> List[List[int]]:
        arr, result = [1,1], [[1], [1,1]]

        if n == 1:
            return [[1]]
        if n == 2:
            return result

        for _ in range(n-2):
            arr = self.__generate(arr)
            result.append(arr)
        return result