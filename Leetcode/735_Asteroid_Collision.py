from typing import List
import pytest

class Solution:
    """This is short and simplified version of below code"""
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            while stack and ast < 0 < stack[-1]:
                if stack[-1] == -ast:
                    stack.pop()
                    break
                elif stack[-1] < -ast:
                    stack.pop()
                    continue
                elif stack[-1] > -ast:
                    break
            else:
                stack.append(ast)
        return stack

    """This is longer and complicated version of above code but still optimized"""
    def asteroidCollision2(self, asteroids: List[int]) -> List[int]:
        stack = []
        for ast in asteroids:
            if ast > 0:
                stack.append(ast)
            else:
                if stack:
                    if stack[-1] < 0:
                        stack.append(ast)
                        continue
                    while stack and stack[-1] <= abs(ast):
                        popped = stack.pop()
                        if popped == abs(ast):
                            break
                        if (not stack and popped < abs(ast)) or (stack and stack[-1] < 0 and popped != abs(ast)):
                            stack.append(ast)
                            break
                else:
                    stack.append(ast)
                    continue
        return stack

def test_case_1():
    sol = Solution()
    assert sol.asteroidCollision([5,10,-5]) == [5,10]

def test_case_2():
    sol = Solution()
    assert sol.asteroidCollision([8,-8]) == []

def test_case_4():
    sol = Solution()
    assert sol.asteroidCollision([8,-9,-1]) == [-9,-1]

def test_case_3():
    sol = Solution()
    assert sol.asteroidCollision([10,2,-5]) == [10]

def test_case_5():
    sol = Solution()
    assert sol.asteroidCollision([-2,-1,1,2]) == [-2,-1,1,2]

def test_case_6():
    sol = Solution()
    assert sol.asteroidCollision([-2,-2,1,-2]) == [-2,-2,-2]

def test_case_7():
    sol = Solution()
    assert sol.asteroidCollision([-2,-2,1,-1]) == [-2,-2]

if __name__ == '__main__':
    pytest.main()