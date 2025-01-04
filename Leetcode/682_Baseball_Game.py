from typing import List
import pytest


class Solution:
    def calPoints(self, operations: List[str]) -> int:
        record = []
        for opn in operations:
            match opn:
                case "+":
                    if record and len(record) >= 2:
                        record.append(sum(record[-2:]))
                case "D":
                    if record and len(record) >= 1:
                        record.append(record[-1] * 2)
                case "C":
                    if record and len(record) >= 1:
                        record.pop()
                case opn:
                    record.append(int(opn))
        return sum(record)

def test_case_1():
    sol = Solution()
    assert sol.calPoints(["5","2","C","D","+"]) == 30

def test_case_2():
    sol = Solution()
    assert sol.calPoints(["5","-2","4","C","D","9","+","+"]) == 27

def test_case_3():
    sol = Solution()
    assert sol.calPoints(["1","C"]) == 0

if __name__ == '__main__':
    pytest.main()