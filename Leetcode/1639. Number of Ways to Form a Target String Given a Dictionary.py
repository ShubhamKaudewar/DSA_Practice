from typing import List

class Solution:
    def numWays1(self, words: List[str], target: str) -> int:
        k = len(target)
        l = len(words[0])
        MOD = 10**9 + 7

        memo = {}
        def dp(p_idx, c_idx, t_idx):
            if t_idx >= k:
                return 1

            if (p_idx, c_idx, t_idx) in memo:
                return memo[(p_idx, c_idx, t_idx)]

            l_cnt = 0
            for child_idx in range(len(words)):
                tc_idx = c_idx
                while l - tc_idx >= k - t_idx:
                    if words[child_idx][tc_idx] == target[t_idx]:
                        l_cnt += dp(child_idx, tc_idx + 1, t_idx + 1)
                        l_cnt %= MOD
                    tc_idx += 1

            memo[(p_idx, c_idx, t_idx)] = l_cnt
            return l_cnt

        res = dp(-1, 0, 0)
        return res

    def numWays2(self, words: List[str], target: str) -> int:
        MOD = 10 ** 9 + 7
        m, n = len(words[0]), len(target)

        # Precompute the frequency of each character at each position
        freq = [[0] * 26 for _ in range(m)]
        for word in words:
            for i, char in enumerate(word):
                freq[i][ord(char) - ord('a')] += 1

        # Initialize dp array
        dp = [0] * (n + 1)
        dp[0] = 1  # Base case: 1 way to form an empty target

        # Fill the dp array
        for i in range(m):
            # Update dp in reverse to avoid overwriting
            for j in range(n, 0, -1):
                char_idx = ord(target[j - 1]) - ord('a')
                dp[j] += dp[j - 1] * freq[i][char_idx]
                dp[j] %= MOD

        return dp[n]


# Example usage:
# solution = Solution()
# print(solution.numWays(["acca","bbbb","caca"], "aba"))  # Output: 6


if __name__ == '__main__':
    sol = Solution()
    # words = ["acca","bbbb","caca"]
    # target = "aba"
    # print(sol.numWays1(words, target))
    words = ["abba","baab"]
    target = "bab"
    print(sol.numWays2(words, target))