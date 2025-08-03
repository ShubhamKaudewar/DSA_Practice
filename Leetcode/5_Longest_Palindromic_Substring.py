import pytest


class Solution:
    """Below one best brute force solution for O(n^3)"""
    def longestPalindrome1(self, s: str) -> str:

        palindrom = ''
        if len(s) == 1:
            return s
        if len(s) == 2:
            if s[0] == s[1]:
                return s

        for first in range(0, len(s)):
            for loop in range(first + 1, len(s) + 1):
                word = s[first:loop]
                if (word == word[::-1] and len(palindrom) <= len(word)):
                    palindrom = word

        return palindrom

    '''
    Below solution use two pointer approach one with odd index and other with even index spread in left and right direction
    Time complexity is O(n^2)
    '''
    def longestPalindrome(self, s: str) -> str:
        longest = 0
        ans = ""
        n = len(s)

        for i in range(n):
            l, r = 0, 0

            while 0 <= i-l <= i+r < n:
                if s[i-l] == s[i+r]:
                    length = (i+r) - (i-l) + 1
                    if length > longest:
                        longest = length
                        ans = s[i-l:i+r+1]

                    l += 1
                    r += 1
                    continue
                break


        for i in range(n):
            l, r = 0, 1

            while 0 <= i-l <= i+r < n:
                if s[i-l] == s[i+r]:
                    length = (i+r) - (i-l) + 1
                    if length > longest:
                        longest = length
                        ans = s[i-l:i+r+1]

                    l += 1
                    r += 1
                    continue
                break

        return ans

    """Below one is Manachar's efficient solution for O(n)"""
    def longestPalindrome2(self, s: str) -> str:
        def preprocess_string(s: str) -> str:
            """Preprocess the string by inserting '#' between characters and adding sentinels."""
            if not s:
                return "^$"
            result = "^"
            for char in s:
                result += "#" + char
            result += "#$"
            return result

        ms = preprocess_string(s)
        n = len(ms)
        p = [0] * n  # palindrome radii array
        center, right = 0, 0
        max_len, max_center = 0, 0

        for i in range(1, n - 1):
            mirror = 2 * center - i

            if i < right:
                p[i] = min(right - i, p[mirror])

            # attempt expansion
            while ms[i + 1 + p[i]] == ms[i - 1 - p[i]]:
                p[i] += 1

            # update center and right if expanded past right boundary
            if i + p[i] > right:
                center, right = i, i + p[i]

            # track max palindrome length and center
            if p[i] > max_len:
                max_len = p[i]
                max_center = i

        # extract longest palindromic substring from original string
        start = (max_center - max_len) // 2
        return s[start:start + max_len]


def test_1():
    sol = Solution()
    s = "babad"
    expected = "bab"
    actual = sol.longestPalindrome(s)
    assert expected == actual

def test_2():
    sol = Solution()
    s = "cbbd"
    expected = "bb"
    actual = sol.longestPalindrome(s)
    assert expected == actual

if __name__ == "__main__":
    pytest.main()