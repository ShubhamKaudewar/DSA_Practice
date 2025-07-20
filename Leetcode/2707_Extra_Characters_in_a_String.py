import pytest
from typing import List
from helper.Trie import TrieNode, Trie

class Solution:
    """Not efficient not not work properly"""
    # def minExtraChar(self, s: str, dictionary: List[str]) -> int:
    #     arr = [True]*len(s)
    #     for w in dictionary:
    #         start = s.find(w)
    #         if start > -1:
    #             for i in range(len(w)):
    #                 arr[start+i] = False
    #
    #     left = float('-inf')
    #     new_left = 0
    #     p = 0
    #
    #     while p<len(s):
    #         if arr[p]:
    #             new_left += 1
    #         else:
    #             left = max(left, new_left) if new_left else left
    #             new_left = 0
    #         p += 1
    #     left = max(left, new_left) if new_left else left
    #     return left

    # SOLUTION-1: USING RECURSION
    def minExtraChar1(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)

        def dfs(i):
            if len(s) == i: #base case when char reach end of string
                return 0

            # Result if total number of character we have to skip, if we skip curr char then rest will be 1+other skips
            res = 1 + dfs(i+1)
            '''we want to check if any of those form word that is contained in a dictionary
            for "abcdef" & ["abc", "bcdef"] after skipping word a we want to check if any substring of bcdef in dict'''
            for j in range(i, len(s)):
                if s[i:i+j] in dictionary:
                    res = min(res, dfs(j+1))
            return res

        return dfs(0)

    # SOLUTION-2: USING RECURSION + MEMOIZATION
    def minExtraChar2(self, s: str, dictionary: List[str]) -> int:
        words = set(dictionary)
        mem = {len(s):0} # cache

        """
        The time complexity of this solution is n^3 (n1 * n2 * n3)
        n1: mem cache till n dfs will get called n time
        n2: for j in range(i, len(s)): will gonna call len(s) which is n
        n3: s[i:i+j] if string is of len n 
        """
        def dfs(i):
            # if len(s) == i: #get rid of this by adding mem[len(s)]=0 pre defined in mem
            #     return 0

            """
            Take e.g. "leetscode" when we skip "l" we have already calculated res for "etscode" (after we skip 1st "e")
            now skipping at e we already have calculated res for "etscode" we can directly use that stored in mem cache
            """
            if i in mem:
                return mem[i]

            # Result if total number of character we have to skip, if we skip curr char then rest will be 1+other skips
            res = 1 + dfs(i+1)
            '''we want to check if any of those form word that is contained in a dictionary
            for "abcdef" & ["abc", "bcdef"] after skipping word a we want to check if any substring of bcdef in dict'''
            for j in range(i, len(s)):
                if s[i:i+j] in words:
                    res = min(res, dfs(j+1))
            mem[i] = res
            return res

        return dfs(0)

    # SOLUTION-2: USING RECURSION + MEMOIZATION
    def minExtraChar(self, s: str, dictionary: List[str]) -> int:
        mem = {len(s): 0}

        trie = Trie()
        for word in dictionary:
            trie.insert(word)


        def dfs(i):
            if i in mem:
                return mem[i]

            res = 1 + dfs(i + 1)
            curr = trie.trieNode
            for j in range(i, len(s)):
                if s[j] not in curr.children:
                    # For e.g. in "leetscode" if s is not in curr node children, there is no way it will have word in dictionary
                    break
                curr = curr.children[s[j]]
                if curr.is_end: # check if entire word match by knowing end of child flag
                    res = min(res, dfs(j + 1))
            mem[i] = res
            return res

        return dfs(0)

def test_case_1():
    sol = Solution()
    s = "leetscode"
    dictionary = ["leet","code","leetcode"]
    expected = 1
    actual = sol.minExtraChar(s, dictionary)
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "sayhelloworld"
    dictionary = ["hello","world"]
    expected = 3
    actual = sol.minExtraChar(s, dictionary)
    assert actual == expected

def test_case_3():
    sol = Solution()
    s = "dwmodizxvvbosxxw"
    dictionary = ["ox","lb","diz","gu","v","ksv","o","nuq","r","txhe","e","wmo","cehy","tskz","ds","kzbu"]
    expected = 7
    actual = sol.minExtraChar(s, dictionary)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()