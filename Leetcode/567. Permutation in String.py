from typing import List
from collections import Counter
from copy import deepcopy

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        s1_map = Counter(s1)
        s1_len = len(s1)

        for head in range(s1_len-1, len(s2)):
            if s2[head] in s1_map:
                sub_s = s2[head-s1_len+1:head+1]
                if Counter(sub_s) == s1_map:
                    return True
        return False

if __name__ == '__main__':
    sol = Solution()
    s1, s2, answer = "ab", "eidbaooo", True
    print(sol.checkInclusion(s1, s2) == answer)
    s1, s2, answer = "ab", "eidboaoo", False
    print(sol.checkInclusion(s1, s2) == answer)
    s1, s2, answer = "adc", "dcda", True
    print(sol.checkInclusion(s1, s2) == answer)
    s1, s2, answer = "hello", "ooolleoooleh", False
    print(sol.checkInclusion(s1, s2) == answer)
    s1, s2, answer = ["snvrcpaywg",
                      "bpzqiabvfoycdesgjqzijqwdgvsetpbxltggvngvitbddfoatgxjgweahffmlfbnrqjxntqoxshzrvwsvchxhlwjablxfxebdlyyogepeoevrozsmuhxtzwuanrzjqsjpfcnoxzmkfskvttwbbijgnvmlvrhusyncngiagjveozhyeyaqgqqwawbckimryslymostqrgbfaqfnzyczijisjwtuvlufvaugeebmkwxrouvzhfujlhwbwhfgkanjkbvoqmtyabcbwrkpuognuyhjzvxktsouwrfpsqrpcrrzqyuvxawkijnoznlxouhuwgwkfuihnjtcklvpgrzzblybnoznhsqyvyjoyzxkdbznhidzuwqbsjjtcsixxfjhvdvsmhtgepexrhddybqncmsomhxjgiruedpsrsasnosxavmomyxhdkeziwapjkscapaerzxstvfygmqdejitsefuiubyzclqtsxjhadtsybhmyrbjtqaxjkmhzwmqndlxuxvsuudnxqpaveddpkqbeziiziywtzazgpinmnzspruzvhelzseioyrdjsqjshmczkvrkqylbmxsrbaxcvisqkfcosonnfbveucnkcinfazivtfbcarkmpkyggiondhpzrcwefsozefgpftoikjwqgyxbyxucjsrmhecuyybqkyipbpxuncpobfmwjlwjluricyzjvrlqtqpdhqfyoezqshascjpqamewpharnsmlfzoorxtpuwpnbkgpzkganupisydhbzfrzhzvanspwrnvcaypomxiwzenytaodqmgeayivdwiifgkpaicihqhgmvjmromkclqrfgpkeoirinccsxvmylxcgqdktusjpxwmqxasmwloxjyjxqqkghqipztfuygkqpkywtywdoxdeljwttcwanolzdacvsnxqbdmbswhzzfzxogpcsxxasgzzqqekabfpnjkkltdrufgukbporvabcbhslxvpdiogmrrtvncqmpykeqaklzwylbvbxlrnwrxosmgdbpilqhbdlbduygiukhflnwoshsmuauiqrwvrpiqekhpziipcphktcwppsvxtrpxiyubxymkzvdnvqazvuhjpayuorhfeknrkwjjzwwycorfjilaabtfgyqpqzxlfrlufdzxujanmyhmalqlkbhnydmbftgcxqitabxhiehmuwauinaukktcubfdhchzmouqfvhzijfitfjbnlnwkupdvqniylsufidhmmszwcipxkktmnruthlxtdnekdjcoxhhyiesazkwqgfusfaevniordhhazhslskhzepyzkpwstea",
                      False]
    print(sol.checkInclusion(s1, s2) == answer)