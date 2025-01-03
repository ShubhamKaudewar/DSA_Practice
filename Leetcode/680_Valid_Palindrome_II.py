from typing import List

class Solution:
    def validPalindrome(self, word: str) -> bool:
        left, right = 0, len(word) - 1

        def _validPalindrome(left, right, c=0):
            nonlocal word
            while left < right:
                if word[left] != word[right]:
                    if c == 1:
                        return False
                    poss1 = _validPalindrome(left, right-1, 1)
                    poss2 = _validPalindrome(left+1, right, 1)
                    return poss1 | poss2
                left += 1
                right -= 1
            return True

        ans = _validPalindrome(left, right)
        return ans


if __name__ == '__main__':
    sol = Solution()
    # s = "aba"
    # print(sol.validPalindrome(s) == True)
    # s = "abca"
    # print(sol.validPalindrome(s) == True)
    s = "abc"
    print(sol.validPalindrome(s) == False)