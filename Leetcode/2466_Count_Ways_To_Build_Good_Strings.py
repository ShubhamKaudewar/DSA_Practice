from typing import List

class Solution:
    def countGoodStrings(self, low: int, high: int, zero: int, one: int) -> int:
        MOD = 10 ** 9 + 7
        dp = [0] * (high + 1) # Creating array to store total valid string for particular length e.g. 11 00 for 2
        dp[0] = 1  # Base case: there's one way to make an empty string

        for length in range(1, high + 1):
            if length >= zero:
                # Incrementing valid string e.g.00 length 2
                dp[length] = (dp[length] + dp[length - zero]) % MOD
            if length >= one:
                # Incrementing valid string e.g.11 length 2
                dp[length] = (dp[length] + dp[length - one]) % MOD

        # Sum up the number of good strings with lengths between low and high
        result = sum(dp[low:high + 1]) % MOD # We want all count i.e. sum of [low, high]
        return result

    # Below string create and modify which is slower in speed not fully optimized
    def countGoodStrings2(self, low: int, high: int, zero: int, one: int) -> int:
        memo = {}

        def dp(cap, acc, char):
            char_map = {"0": zero, "1": one}

            if char in char_map:
                if cap >= char_map[char]:
                    acc += char * char_map[char]
                    cap -= char_map[char]
                else:
                    return 0

            count = 0
            if low <= len(acc) <= high:
                count += 1
            if not cap:
                return count

            memo[(cap, acc, char)] = count + dp(cap, acc, "0") + dp(cap, acc, "1")
            return memo[(cap, acc, char)]
        return dp(high, "", "")

if __name__ == '__main__':
    sol = Solution()
    # low, high, zero, one = 3, 3, 1, 1
    # low, high, zero, one = 2, 3, 1, 2
    low, high, zero, one = 200, 200, 10, 1
    print(sol.countGoodStrings(low, high, zero, one))