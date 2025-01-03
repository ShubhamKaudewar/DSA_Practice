from typing import List

class Solution:
    def vowelStrings(self, words: List[str], queries: List[List[int]]) -> List[int]:
        vowels = {"a": True, "e": True, "i": True, "o": True, "u": True}
        prefixSum = [0] * (len(words) + 1)
        total = 0
        for idx, word in enumerate(words):
            factor = 0
            if word[0] in vowels and word[-1] in vowels:
                factor = 1
            prefixSum[idx+1] = total+factor
            total += factor

        res = []
        for s, e in queries:
            s, e = s+1, e+1
            if s == e:
                res.append(0 if prefixSum[s] == prefixSum[s-1] else 1)
                continue
            count = prefixSum[e] - prefixSum[s-1]
            res.append(count)
        return res


if __name__ == "__main__":
    sol = Solution()
    # words, queries = ["omo", "illi", "on", "aire"], [[2, 2], [1, 3]]
    # print(sol.vowelStrings(words, queries) == [0, 2])
    words, queries = ["aba", "bcb", "ece", "aa", "e"], [[0, 2], [1, 4], [1, 1]]
    print(sol.vowelStrings(words, queries) == [2,3,0])
    # words, queries = ["a","e","i"], [[0,2],[0,1],[2,2]]
    # print(sol.vowelStrings(words, queries) == [3,2,1])
    # words = ["b", "rmivyakd", "kddwnexxssssnvrske", "vceguisunlxtldqenxiyfupvnsxdubcnaucpoi", "nzwdiataxfkbikbtsjvcbjxtr",
    #  "wlelgybcaakrxiutsmwnkuyanvcjczenuyaiy", "eueryyiayq", "bghegfwmwdoayakuzavnaucpur", "ukorsxjfkdojcxgjxgmxbghno",
    #  "pmgbiuzcwbsakwkyspeikpzhnyiqtqtfyephqhl", "gsjdpelkbsruooeffnvjwtsidzw", "ugeqzndjtogxjkmhkkczdpqzwcu",
    #  "ppngtecadjsirj", "rvfeoxunxaqezkrlr", "adkxoxycpinlmcvmq", "gfjhpxlzmokcmvhjcrbrpfakspscmju", "rgmzhaj",
    #  "ychktzwdhfuruhpvdjwfsqjhztshcxdey", "yifrzmmyzvfk", "mircixfzzobcficujgbj", "d",
    #  "pxcmwnqknyfkmafzbyajjildngccadudfziknos", "dxmlikjoivggmyasaktllgmfhqpyznc", "yqdbiiqexkemebyuitve"]
    # queries = [[5, 21],[17, 22],[19, 23],[13, 15],[20, 23],[21, 23],[6, 20],[1, 8],[15, 20],[17, 22],[6, 6],[1, 2],
    #            [4, 11],[14, 23],[7, 10],[16, 22],[20, 22],[21, 22],[15, 18],[5, 16],[17, 23]]
    # print(sol.vowelStrings(words, queries) == [2,0,0,0,0,0,2,1,0,0,0,0,2,0,1,0,0,0,0,2,0])

