import pytest
from typing import List

class Solution:
    def shift(self, word, prefixSum):
        # Perform the character shifting based on prefix sums
        return ''.join(chr(((ord(c) - ord('a') + p) % 26) + ord('a')) for c, p in zip(word, prefixSum))

    def shiftingLetters(self, word: str, shifts: List[List[int]]) -> str:
        n = len(word)
        prefixSum = [0] * (n + 1)  # Extra element to simplify the range operations

        # Update the range shifts using the prefix sum array
        for s, e, d in shifts:
            direction = -1 if d == 0 else 1
            prefixSum[s] += direction  # Start range
            prefixSum[e + 1] -= direction  # End range + 1

        # Calculate cumulative sums for the shifts
        for i in range(1, n):
            prefixSum[i] += prefixSum[i - 1]

        # Shift letters and return the result
        return self.shift(word, prefixSum[:-1])  # Exclude the extra element at the end

# Test cases
def test_case_1():
    sol = Solution()
    assert sol.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"


def test_case_2():
    sol = Solution()
    assert sol.shiftingLetters("dztz", [[0, 0, 0], [1, 1, 1]]) == "catz"


if __name__ == "__main__":
    pytest.main()


def test_case_1():
    sol = Solution()
    assert sol.shiftingLetters("abc", [[0, 1, 0], [1, 2, 1], [0, 2, 1]]) == "ace"

def test_case_2():
    sol = Solution()
    assert sol.shiftingLetters("dztz", [[0,0,0],[1,1,1]]) == "catz"

if __name__ == '__main__':
    pytest.main()