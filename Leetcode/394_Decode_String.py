import pytest

class Solution:
    """Using stack more optimized no need of recursion"""
    def decodeString(self, s: str) -> str:
        stack, num, current = [], 0, ""
        for char in s:
            if char.isdigit():
                num = num * 10 + int(char)
            elif char == "[":
                stack.append((current, num))
                current, num = "", 0
            elif char == "]":
                prev_str, repeat = stack.pop()
                current = prev_str + current * repeat
            else:
                current += char
        return current

    """Using recursion"""
    def decodeString2(self, s: str) -> str:
        def dp(s):
            i, res = 0, ""

            while i < len(s):
                if s[i].isnumeric():
                    int_val, sub_s, c = 0, "", 1

                    while s[i].isnumeric():
                        int_val = int_val*10 + int(s[i])
                        i += 1
                    i += 1

                    while c > 0:
                        if s[i] == "]":
                            c -= 1
                        elif s[i] == "[":
                            c += 1
                        sub_s += s[i]
                        i += 1
                    res += int_val * dp(sub_s[:-1])
                elif s[i].isalpha():
                    res += s[i]
                    i += 1
            return res
        return dp(s)

def test_case_1():
    sol = Solution()
    assert sol.decodeString("3[a]2[bc]") == "aaabcbc"

def test_case_2():
    sol = Solution()
    assert sol.decodeString("3[a2[c]]") == "accaccacc"
#
def test_case_3():
    sol = Solution()
    assert sol.decodeString("2[abc]3[cd]ef") == "abcabccdcdcdef"

def test_case_4():
    sol = Solution()
    assert sol.decodeString("100[leetcode]") == 100*"leetcode"

if __name__ == '__main__':
    pytest.main()