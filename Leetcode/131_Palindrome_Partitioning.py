import pytest
from typing import List

class Solution:
    def partition(self, s: str) -> List[List[str]]:
        """
        This is question of backtracking from neetcode 150
        :param s: string to be optimally partitioned into characters and words
        :return: The list of combination of characters and word split optimally which every individual is palindrome
        """
        result = []
        if len(s) == 1:
            result.append([s])
            return result

        for i in range(len(s)):
            part_1 = s[:i+1]
            part_2 = s[i+1:]
            if part_1 == part_1[::-1]:
                childs = self.partition(part_2)
                if not childs:
                    result.append([part_1])
                else:
                    for child in childs:
                        result.append([part_1, *child])
        return result


def test_case_1():
    sol = Solution()
    s = "aab"
    expected = [["a","a","b"],["aa","b"]]
    actual = sol.partition(s)
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "a"
    expected = [["a"]]
    actual = sol.partition(s)
    assert actual == expected
#
def test_case_3():
    sol = Solution()
    s = "abcaa"
    expected = [["a","b","c","a","a"],["a","b","c","aa"]]
    actual = sol.partition(s)
    assert actual == expected

if __name__ == '__main__':
    pytest.main()