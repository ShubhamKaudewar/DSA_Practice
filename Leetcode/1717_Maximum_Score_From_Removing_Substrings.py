import pytest
from typing import List

class Solution:
    def __init__(self):
        self.mem = {}
        self.counter = 0

    def maximumGain1(self, s: str, x: int, y: int) -> int:
        self.counter += 1
        """
        This question is of greedy and dp, where greedy is optimal
        below approach is for dp using memo, with 3rd test case it gives TLE
        You're exploring all possible pairs of "ab" and "ba" combinations in every possible order.
        Every recursion creates a new string (s[:i] + s[i+2:]), which is an expensive operation and creates many distinct states.
        The memoization dictionary helps some, but not enough when substring states can number in the hundreds of thousands.
        """
        if s in self.mem:
            return self.mem[s]

        ans = 0
        for i in range(len(s)):
            if s[i:i+2] == "ab":
                curr = x + self.maximumGain1(s[:i]+s[i+2:], x, y)
                ans = max(ans, curr)
            if s[i:i+2] == "ba":
                curr = y + self.maximumGain1(s[:i]+s[i+2:], x, y)
                ans = max(ans, curr)

        if s not in self.mem:
            self.mem[s] = ans

        return ans

    def maximumGain(self, s: str, x: int, y: int) -> int:
        """
        This is a classic case of greedy string reduction, where it's better to remove the more profitable substrings first.
        If x > y, prioritize removing "ab" first. Otherwise, remove "ba" first.
        """
        def remove_pair(s, first, second, score):
            stack = []
            total = 0
            for c in s:
                if stack and stack[-1] == first and c == second:
                    stack.pop()
                    total += score
                else:
                    stack.append(c)
            return total, "".join(stack)

        # First remove the more profitable pair
        if x >= y:
            gain1, rem = remove_pair(s, "a", "b", x)
            gain2, _ = remove_pair(rem, "b", "a", y)
        else:
            gain1, rem = remove_pair(s, "b", "a", y)
            gain2, _ = remove_pair(rem, "a", "b", x)

        return gain1 + gain2

def test_case_1():
    sol = Solution()
    s = "cdbcbbaaabab"
    x = 4
    y = 5
    expected = 19
    actual = sol.maximumGain(s, x, y)
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "aabbaaxybbaabb"
    x = 5
    y = 4
    expected = 20
    actual = sol.maximumGain(s, x, y)
    assert actual == expected

def test_case_3():
    sol = Solution()
    s = "aabbrtababbabmaaaeaabeawmvaataabnaabbaaaybbbaabbabbbjpjaabbtabbxaaavsmmnblbbabaeuasvababjbbabbabbasxbbtgbrbbajeabbbfbarbagha"
    x = 8484
    y = 4096
    expected = 198644
    actual = sol.maximumGain(s, x, y)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()