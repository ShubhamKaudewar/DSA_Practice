import pytest

class Solution:
    """
    This approach utilize two pointer solution, expands left and right.
    https://www.youtube.com/watch?v=4RACzI5-du8
    """
    def countSubstrings(self, s: str) -> int:
        count = 0
        n = len(s)

        for idx, c in enumerate(s):
            l, r = 0, 0

            while 0 <= idx-l <= idx+r < n:
                if s[idx-l] == s[idx+r]:
                    count += 1
                    l += 1
                    r += 1
                    continue
                break


        for idx, c in enumerate(s):
            l, r = 0, 1
            while 0 <= idx-l <= idx+r < n:
                if s[idx-l] == s[idx+r]:
                    count += 1
                    l += 1
                    r += 1
                    continue
                break

        return count

    """
    Below is brute force and have O(n^2) complexity, this can be optimized using two pointer solution
    """
    def countSubstrings1(self, s: str) -> int:
        l, r = 0, 1
        n = len(s)
        count = 0

        while l < n:
            if s[l:r] == s[l:r][::-1]:
                count += 1
            r += 1

            if r > n:
                l += 1
                r = l+1
        return count

def test_1():
    sol = Solution()
    s = "abc"
    expected = 3
    actual = sol.countSubstrings(s)
    assert expected == actual

def test_2():
    sol = Solution()
    s = "aaa"
    expected = 6
    actual = sol.countSubstrings(s)
    assert expected == actual

def test_3():
    sol = Solution()
    s = "aaab"
    expected = 7
    actual = sol.countSubstrings(s)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()