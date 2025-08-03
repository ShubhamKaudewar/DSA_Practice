import pytest

class Solution:
    """Need to use memo to avoid TLE"""
    def numDecodings(self, s: str) -> int:
        map_set = set(str(i) for i in range(1, 27))
        memo = {}  # cache for substring results

        def backtrack(subs):
            if subs in memo:
                return memo[subs]

            if not subs:  # reached end means valid decoding
                return 1

            if subs[0] == "0": # no decoding start with 0
                return 0

            count = 0
            for i in range(1, 3):
                if i <= len(subs) and subs[:i] in map_set:
                    count += backtrack(subs[i:])

            memo[subs] = count
            return count

        return backtrack(s)

    """Without memoization below code get TLE on test case 6"""
    def numDecodings1(self, s: str) -> int:
        map_set = set(str(i) for i in range(1, 27))
        count = 0

        def backtrack(s):
            nonlocal count

            if not s or (len(s) == 1 and s in map_set):
                count += 1
                return

            for i in range(1, 3):
                if s[:i] in map_set:
                    backtrack(s[i:])

        backtrack(s)
        return count



def test_1():
    sol = Solution()
    s = "12"
    expected = 2
    actual = sol.numDecodings(s)
    assert expected == actual

def test_2():
    sol = Solution()
    s = "226"
    expected = 3
    actual = sol.numDecodings(s)
    assert expected == actual

def test_3():
    sol = Solution()
    s = "06"
    expected = 0
    actual = sol.numDecodings(s)
    assert expected == actual

def test_4():
    sol = Solution()
    s = "11106"
    expected = 2
    actual = sol.numDecodings(s)
    assert expected == actual

def test_5():
    sol = Solution()
    s = "0"
    expected = 0
    actual = sol.numDecodings(s)
    assert expected == actual

def test_6():
    sol = Solution()
    s = "111111111111111111111111111111111111111111111"
    expected = 1836311903
    actual = sol.numDecodings(s)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()