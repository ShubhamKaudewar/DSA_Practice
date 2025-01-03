from typing import List


class Solution:
    def maxScore(self, word: str) -> int:
        one_c = sum(int(char) for char in word)

        max_s = 0
        zero_c = 0
        for i in range(len(word)-1):
            if word[i] == "0":
                zero_c += 1
            else:
                one_c -= 1
            max_s = max(max_s, one_c + zero_c)
        return max_s

if __name__ == '__main__':
    sol = Solution()
    s = "011101"
    print(sol.maxScore(s))
    s = "00111"
    print(sol.maxScore(s))
    s = "1111"
    print(sol.maxScore(s))
    # s = "00"
    # print(sol.maxScore(s))