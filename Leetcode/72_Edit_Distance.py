import pytest

class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        cache = [[float("inf")] * (len(word2)+1) for _ in range(len(word1) + 1)]

        # Filling extra border cell values
        for j in range(len(word2) + 1):
            cache[len(word1)][j] = len(word2) - j
        for i in range(len(word1) + 1):
            cache[i][len(word2)] = len(word1) - i

        for i in range(len(word1)-1, -1, -1):
            for j in range(len(word2)-1, -1, -1):
                if word1[i] == word2[j]:
                    cache[i][j] = cache[i+1][j+1] # On char match take diagonal value and 0 operation
                else:
                    cache[i][j] = 1 + min(cache[i][j+1], cache[i+1][j], cache[i+1][j+1])  # On char match take diagonal value and 0 operation

        return cache[0][0]



def test_case_1():
    sol = Solution()
    word1 = "horse"
    word2 = "ros"
    expected = 3
    actual = sol.minDistance(word1, word2)
    assert actual == expected

def test_case_2():
    sol = Solution()
    word1 = "intention"
    word2 = "execution"
    expected = 5
    actual = sol.minDistance(word1, word2)
    assert actual == expected


if __name__ == '__main__':
    pytest.main()

