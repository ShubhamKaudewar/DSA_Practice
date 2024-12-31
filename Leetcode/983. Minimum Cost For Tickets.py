from typing import List

class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        dp = [0] * (len(days) + 1)
        for p in range(len(days)-1, -1, -1):
            min_cost = float('inf')
            for ticket, cost in zip((1, 7, 30), costs):
                if ticket == 1:
                    curr_cost = cost + dp[p+1]
                    min_cost = min(min_cost, curr_cost)
                else:
                    l = p
                    while l < len(days) and l <= ticket+p:
                        if days[l] >= days[p]+ticket:
                            break
                        if l == len(days):
                            break
                        l += 1
                    curr_cost = cost + dp[l]
                    min_cost = min(min_cost, curr_cost)
            dp[p] = min_cost
        return dp[0]

if __name__ == '__main__':
    sol = Solution()
    # days = [1,4,6,7,8,20]
    # costs = [2,7,15]
    # days = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 30, 31]
    # costs = [2, 7, 15]
    days = [1,2,3,4,6,8,9,10,13,14,16,17,19,21,24,26,27,28,29]
    costs = [3,14,50]
    print(sol.mincostTickets(days, costs))