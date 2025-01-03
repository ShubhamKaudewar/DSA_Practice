from typing import List

class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        boats = 0
        people.sort()
        small, big = 0, len(people) - 1

        """This code work for 2 people max case but n people max then it does not work"""
        while small <= big:
            if people[small] + people[big] <= limit:
                small += 1
            big -= 1
            boats += 1

        """This code works when there are more than 2 people head count"""
        # capacity, head = limit, 0
        # while small <= big:
        #     if capacity > 0 and head < 2:
        #         if people[big] <= capacity and head < 2:
        #             capacity -= people[big]
        #             big -= 1
        #             head += 1
        #         elif people[small] <= capacity:
        #             capacity -= people[small]
        #             small += 1
        #             head += 1
        #         else:
        #             capacity, head = limit, 0
        #             boats += 1
        #     if capacity == 0 or big < small or head >= 2:
        #         capacity, head = limit, 0
        #         boats += 1

        return boats

if __name__ == '__main__':
    sol = Solution()
    # people, limit, answer = [1, 2], 3, 1
    # print(sol.numRescueBoats(people, limit) == answer)
    # people, limit, answer = [3,2,2,1], 3, 3
    # print(sol.numRescueBoats(people, limit) == answer)
    # people, limit, answer = [3,5,3,4], 5, 4
    # print(sol.numRescueBoats(people, limit) == answer)
    people, limit, answer = [3,2,3,2,2], 6, 3
    print(sol.numRescueBoats(people, limit) == answer)