import pytest

class Solution:
    """This is question of dp, require memoization for 2D to store possible ans from that point
    Approach is by skipping or taking character, this is 0/1 knapsack problem"""
    def numDistinct(self, s: str, t: str) -> int:
        cache = {}

        def dfs(i, j) -> int:
            if (i, j) in cache:
                return cache[(i,j)]

            if j >= len(t): # j pointer in target out of bound means we got the solution
                return 1
            if i >= len(s): # i pointer in target out of bound means no more char available to match rest of t[j::]
                return 0

            if s[i] == t[j]:
                count1 = dfs(i+1, j+1) # take the char in s
                count2 = dfs(i+1, j) # skip the char in s
                count = count1 + count2
            else:
                count = dfs(i+1, j)

            cache[(i, j)] = count
            return cache[(i, j)]

        return dfs(0, 0)



# def test_case_1():
#     sol = Solution()
#     s = "rabbbit"
#     t = "rabbit"
#     expected = 3
#     actual = sol.numDistinct(s, t)
#     assert actual == expected
#
# def test_case_2():
#     sol = Solution()
#     s = "babgbag"
#     t = "bag"
#     expected = 5
#     actual = sol.numDistinct(s, t)
#     assert actual == expected
# #
#
# def test_case_3():
#     sol = Solution()
#     s = "caaat"
#     t = "cat"
#     expected = 3
#     actual = sol.numDistinct(s, t)
#     assert actual == expected
#
# def test_case_4():
#     sol = Solution()
#     s = "a"
#     t = ""
#     expected = 1
#     actual = sol.numDistinct(s, t)
#     assert actual == expected
#
# def test_case_5():
#     sol = Solution()
#     s = ""
#     t = ""
#     expected = 1
#     actual = sol.numDistinct(s, t)
#     assert actual == expected

def test_case_6():
    sol = Solution()
    s = ""
    t = "a"
    expected = 0
    actual = sol.numDistinct(s, t)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()

