import pytest
from typing import List
from helper import Graph

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        """Hierholzer's Algorithm (Recursion)"""
        tickets.sort(reverse=True)
        adj_map = Graph().construct_adjacency_list(0, tickets)
        res = []

        def dfs(src):
            while adj_map[src]:
                dst = adj_map[src].pop()
                dfs(dst)
            res.append(src)

        dfs('JFK')
        return res[::-1]

    def findItinerary2(self, tickets: List[List[str]]) -> List[str]:
        tickets.sort()
        adj_map = Graph().construct_adjacency_list(0, tickets)
        res = ["JFK"]

        def dfs(src):
            if len(res) == len(tickets) + 1: # base case that we found one path
                return True

            if src not in adj_map: # There is no outgoing path from src we are stuck
                return False

            temp = list(adj_map[src])
            for idx, nei in enumerate(temp):
                adj_map[src].pop(idx)
                res.append(nei)

                if dfs(nei):
                    return True  # Return as we know we found one such path

                adj_map[src].insert(idx, nei)
                res.pop()
            return False

        dfs("JFK")
        return res


def test_case_1():
    sol = Solution()
    tickets = [["MUC","LHR"],["JFK","MUC"],["SFO","SJC"],["LHR","SFO"]]
    actual = sol.findItinerary(tickets)
    expected = ["JFK","MUC","LHR","SFO","SJC"]
    assert actual == expected

def test_case_2():
    sol = Solution()
    tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
    actual = sol.findItinerary(tickets)
    expected = ["JFK","ATL","JFK","SFO","ATL","SFO"]
    assert actual == expected



if __name__ == '__main__':
    pytest.main()