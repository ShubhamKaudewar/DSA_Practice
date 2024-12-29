from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        res = 0
        count = defaultdict(lambda: 0)
        l = 0
        for r in range(len(s)):
            count[s[r]] += 1
            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            res = max(res, r - l + 1)
        return res

if __name__ == '__main__':
    sol = Solution()
    s = "ABAB"
    k = 2
    print(sol.characterReplacement(s, k))