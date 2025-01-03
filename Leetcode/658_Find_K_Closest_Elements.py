from typing import List
from collections import Counter

class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        s1_map = Counter(s1)
        s1_len = len(s1)

        for head in range(s1_len-1, len(s2)):
            if s2[head] in s1_map:
                sub_s = s2[head-s1_len+1:head+1]
                if Counter(sub_s) == s1_map:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    arr, k, x, answer = [1,2,3,4,5], 4, 3, [1,2,3,4]
    print(sol.findClosestElements(arr, k, x) == answer)