from typing import List
class Solution:
    def maxScoreSightseeingPair(self, values: List[int]) -> int:
        max_i = values[0] + 0
        max_s = 0
        for i in range(1, len(values)):
            max_s = max(max_s, max_i + values[i] - i)
            max_i = max(max_i, values[i] + i)
        return max_s


if __name__ == '__main__':
    sol = Solution()
    values = [8,1,5,2,6]
    print(sol.maxScoreSightseeingPair(values))