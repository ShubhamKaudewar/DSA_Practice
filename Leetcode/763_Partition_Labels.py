import pytest
from typing import List
from collections import defaultdict

class Solution:
    """
    This is question of greedy, this is window size problem. We will start window size from 0 and then keep increasing until
    we have all the elements from start(0 initially) to start+size window in that range only. We can chake this by checking against
    present character inside range last present index hash map lookup
    """
    def partitionLabels(self, s: str) -> List[int]:
        start = 0
        end_map = defaultdict(int)
        ans = []

        for idx, chr in enumerate(s):
            end_map[chr] = idx

        while start < len(s):
            p = start
            size = start
            partition = False
            while p <= size:
                if end_map[s[p]] > size:
                    size = max(size, end_map[s[p]])
                    continue
                if p == size:
                    partition = True
                    break
                p += 1
            if partition:
                ans.append(size+1-start)
                start = p+1

        return ans


def test_case_1():
    sol = Solution()
    s = "ababcbacadefegdehijhklij"
    actual = sol.partitionLabels(s)
    expected = [9,7,8]
    assert actual == expected

def test_case_2():
    sol = Solution()
    s = "eccbbbbdec"
    actual = sol.partitionLabels(s)
    expected = [10]
    assert actual == expected

def test_case_3():
    sol = Solution()
    s = "xyxxyzbzbbisl"
    actual = sol.partitionLabels(s)
    expected = [5, 5, 1, 1, 1]
    assert actual == expected

def test_case_4():
    sol = Solution()
    s = "abcabc"
    actual = sol.partitionLabels(s)
    expected = [6]
    assert actual == expected


if __name__ == '__main__':
    pytest.main()