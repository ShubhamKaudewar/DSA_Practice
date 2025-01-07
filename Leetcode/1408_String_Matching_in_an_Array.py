
from typing import List
import pytest

class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        output = []
        for i in range(len(words)):
            for j in range(len(words)):
                if i == j:
                    continue
                if words[i] in words[j]:
                    output.append(words[i])
                    break
        return output

def test_case_1():
    sol = Solution()
    assert sol.stringMatching(["mass","as","hero","superhero"]) == ["as","hero"]

def test_case_2():
    sol = Solution()
    assert sol.stringMatching(["leetcode","et","code"]) == ["et","code"]

def test_case_3():
    sol = Solution()
    assert sol.stringMatching(["blue","green","bu"]) == []

def test_case_4():
    sol = Solution()
    words = ["uexk","aeuexkf","wgxih","yuexk","gxea","yuexkm","ypmfx","jjuexkmb","wqpri","aeuexkfpo","kqtnz","pkqtnza","nrbb","hmypmfx","krqs","jjuexkmbyt","zvru","ypmfxj"]
    expected = ["uexk","aeuexkf","yuexk","ypmfx","jjuexkmb","kqtnz"]
    actual = sol.stringMatching(words)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()