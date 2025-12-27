from collections import deque
import pytest

class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        n = len(senate)
        radiant = deque()
        dire = deque()

        for i, c in enumerate(senate):
            if c == "R":
                radiant.append(i)
            else:
                dire.append(i)

        while radiant and dire:
            r = radiant.popleft()
            d = dire.popleft()
            if r < d:
                radiant.append(r + n)  # R bans D, comes back later
            else:
                dire.append(d + n)     # D bans R, comes back later

        return "Radiant" if radiant else "Dire"

    def predictPartyVictory1(self, senate: str) -> str:
        senate = list(senate)

        while True:
            curr = senate[0]
            if senate.count(curr) == len(senate):
                return "Radiant" if curr == "R" else "Dire"
            senate.pop(senate.index("D" if curr == "R" else "R"))
            senate.pop(0)
            senate.append(curr)

    def predictPartyVictory2(self, senate: str) -> str:
        n = len(senate)
        curr = senate[0]

        if senate.count(curr) == n:
            return "Radiant" if curr == "R" else "Dire"

        for idx, senator in enumerate(senate):
            if senator != curr:
                senate = senate[1:idx] + senate[idx+1:] + curr
                break

        return self.predictPartyVictory(senate)


def test_case_1():
    sol = Solution()
    senate = "RD"
    actual = sol.predictPartyVictory(senate)
    expected = "Radiant"
    assert actual == expected

def test_case_2():
    sol = Solution()
    senate = "RDD"
    actual = sol.predictPartyVictory(senate)
    expected = "Dire"
    assert actual == expected

def test_case_3():
    sol = Solution()
    senate = "DDRRR"
    actual = sol.predictPartyVictory(senate)
    expected = "Dire"
    assert actual == expected

if __name__ == '__main__':
    pytest.main()