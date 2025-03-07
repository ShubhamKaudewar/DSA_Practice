
from typing import List
from collections import defaultdict
from copy import deepcopy

class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        if set(words) == set(s):
            return [i for i in range(len(s)-len(words)+1)]

        result = []
        master_d = defaultdict(lambda: 0)
        for word in words:
            master_d[word] += 1

        slide_wl = len(words[0])
        tot_words = len(words)
        concat_wl = slide_wl * tot_words

        for i in range(len(s) - concat_wl + 1):
            local_d = dict(deepcopy(master_d))

            for j in range(tot_words):
                w_check = s[i+(slide_wl*j):i+(slide_wl*(j+1))]
                if local_d.get(w_check):
                    local_d[w_check] -= 1
                    if local_d[w_check] == 0:
                        del local_d[w_check]
                    continue
                break
            if not local_d:
                result.append(i)
        return result


sol = Solution()
s = "lingmindraboofooowingdingbarrwingmonkeypoundcake"
words = ["fooo","barr","wing","ding","wing"]
# s = "barfoothefoobarman"
# words = ["foo","bar"]
# s = "wordgoodgoodgoodbestword"
# words = ["word","good","best","word"]
# s = "barfoofoobarthefoobarman"
# words = ["bar","foo","the"]
print(sol.findSubstring(s, words))