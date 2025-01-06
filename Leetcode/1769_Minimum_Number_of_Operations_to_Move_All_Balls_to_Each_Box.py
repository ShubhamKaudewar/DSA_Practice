from typing import List
import pytest

class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        prefixArr = list(boxes)
        ballArr = [idx for idx, val in enumerate(prefixArr) if val == "1"]
        output = []

        for i in range(len(prefixArr)):
            res = 0
            for j in ballArr:
                if j == i: continue
                res += abs(i-j)
            output.append(res)
        return output

def test_case_1():
    sol = Solution()
    assert sol.minOperations("001011") == [11,8,5,4,3,4]

def test_case_2():
    sol = Solution()
    assert sol.minOperations("110") == [1,1,3]

if __name__ == '__main__':
    pytest.main()