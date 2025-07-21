from typing import List

import pytest


class Solution:
    def makeFancyString(self, s: str) -> str:
        """
        To solve this question use StringBuilder: use another string to build result
        if you intend to use same string -> list & pop it will result in TLE
        """
        if len(s) < 3:
            return s

        result = s[0]
        chars = list(s)
        p = 1
        
        while p < len(chars)-1:
            if chars[p-1] != chars[p] or chars[p] != chars[p+1]:
                result += chars[p]
            p += 1
        return result + chars[-1]
            
        
        
def test_case_1():
    sol = Solution()
    s = "leeetcode"
    expected = "leetcode"
    actual = sol.makeFancyString(s)
    assert actual == expected
    
def test_case_2():
    sol = Solution()
    s = "aaabaaaa"
    expected = "aabaa"
    actual = sol.makeFancyString(s)
    assert actual == expected
    
def test_case_3():
    sol = Solution()
    s = "aab"
    expected = "aab"
    actual = sol.makeFancyString(s)
    assert actual == expected
    
def test_case_4():
    sol = Solution()
    s = "a"
    expected = "a"
    actual = sol.makeFancyString(s)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()