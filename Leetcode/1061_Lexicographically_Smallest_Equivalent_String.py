import pytest
from helper import CharUnionFindDirect
            
class Solution:
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str) -> str:
        """
        This is question of union find algorithm, to perform set operations
        Example here: https://www.geeksforgeeks.org/introduction-to-disjoint-set-data-structure-or-union-find-algorithm/
        Union Find Algorithm Explanation: https://yuminlee2.medium.com/union-find-algorithm-ffa9cd7d2dba
        """
        uf = CharUnionFindDirect()
        for c1, c2 in zip(s1, s2):
            uf.union(c1, c2)
        
        answer = "".join(uf.find(c) for c in baseStr)
        return answer

def test_case_1():
    sol = Solution()
    s1 = "parker"
    s2 = "morris"
    baseStr = "parser"
    result = sol.smallestEquivalentString(s1, s2, baseStr)
    ans_str = "makkek"
    assert result == ans_str

def test_case_2():
    sol = Solution()
    s1 = "leetcode"
    s2 = "programs"
    baseStr = "sourcecode"
    result = sol.smallestEquivalentString(s1, s2, baseStr)
    ans_str = "aauaaaaada"
    assert result == ans_str

if __name__ == '__main__':
    pytest.main()