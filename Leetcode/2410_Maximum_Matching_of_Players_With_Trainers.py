import pytest

class Solution:
    def matchPlayersAndTrainers(self, players, trainers):
        players.sort() #[4,7,9]
        trainers.sort() #[2,5,8,8]
        match = 0
        p, t = 0, 0

        while p < len(players) and t < len(trainers):
            if players[p] <= trainers[t]:
                match += 1
                p += 1
            t += 1
        return match

# def test_case_1():
#     sol = Solution()
#     players = [4,7,9]
#     trainers = [8,2,5,8]
#     expected = 2
#     actual = sol.matchPlayersAndTrainers(players, trainers)
#     assert actual == expected
#
# def test_case_2():
#     sol = Solution()
#     players = [1,1,1]
#     trainers = [10]
#     expected = 1
#     actual = sol.matchPlayersAndTrainers(players, trainers)
#     assert actual == expected
#
def test_case_3():
    sol = Solution()
    players = [2]
    trainers = [1]
    expected = 0
    actual = sol.matchPlayersAndTrainers(players, trainers)
    assert actual == expected

# def test_case_4():
#     sol = Solution()
#     players = [1,1000000000]
#     trainers = [1000000000,1]
#     expected = 2
#     actual = sol.matchPlayersAndTrainers(players, trainers)
#     assert actual == expected

if __name__ == '__main__':
    pytest.main()