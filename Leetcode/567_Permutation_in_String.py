from typing import List
from collections import Counter
import pytest

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

def test_checkInclusion():
    sol = Solution()
    assert sol.checkInclusion("ab", "eidbaooo") == True
    assert sol.checkInclusion("ab", "eidboaoo") == False
    assert sol.checkInclusion("adc", "dcda") == True
    assert sol.checkInclusion("hello", "ooolleoooleh") == False
    assert sol.checkInclusion("snvrcpaywg", "bpzqiabvfoycdesgjqzijqwdgvsetpbxltggvngvitbddfoatgxjgweahffmlfbnrqjxntqoxshzrvwsvchxhlwjablxfxebdlyyogepeoevrozsmuhxtzwuanrzjqsjpfcnoxzmkfskvttwbbijgnvmlvrhusyncngiagjveozhyeyaqgqqwawbckimryslymostqrgbfaqfnzyczijisjwtuvlufvaugeebmkwxrouvzhfujlhwbwhfgkanjkbvoqmtyabcbwrkpuognuyhjzvxktsouwrfpsqrpcrrzqyuvxawkijnoznlxouhuwgwkfuihnjtcklvpgrzzblybnoznhsqyvyjoyzxkdbznhidzuwqbsjjtcsixxfjhvdvsmhtgepexrhddybqncmsomhxjgiruedpsrsasnosxavmomyxhdkeziwapjkscapaerzxstvfygmqdejitsefuiubyzclqtsxjhadtsybhmyrbjtqaxjkmhzwmqndlxuxvsuudnxqpaveddpkqbeziiziywtzazgpinmnzspruzvhelzseioyrdjsqjshmczkvrkqylbmxsrbaxcvisqkfcosonnfbveucnkcinfazivtfbcarkmpkyggiondhpzrcwefsozefgpftoikjwqgyxbyxucjsrmhecuyybqkyipbpxuncpobfmwjlwjluricyzjvrlqtqpdhqfyoezqshascjpqamewpharnsmlfzoorxtpuwpnbkgpzkganupisydhbzfrzhzvanspwrnvcaypomxiwzenytaodqmgeayivdwiifgkpaicihqhgmvjmromkclqrfgpkeoirinccsxvmylxcgqdktusjpxwmqxasmwloxjyjxqqkghqipztfuygkqpkywtywdoxdeljwttcwanolzdacvsnxqbdmbswhzzfzxogpcsxxasgzzqqekabfpnjkkltdrufgukbporvabcbhslxvpdiogmrrtvncqmpykeqaklzwylbvbxlrnwrxosmgdbpilqhbdlbduygiukhflnwoshsmuauiqrwvrpiqekhpziipcphktcwppsvxtrpxiyubxymkzvdnvqazvuhjpayuorhfeknrkwjjzwwycorfjilaabtfgyqpqzxlfrlufdzxujanmyhmalqlkbhnydmbftgcxqitabxhiehmuwauinaukktcubfdhchzmouqfvhzijfitfjbnlnwkupdvqniylsufidhmmszwcipxkktmnruthlxtdnekdjcoxhhyiesazkwqgfusfaevniordhhazhslskhzepyzkpwstea") == False

if __name__ == '__main__':
    pytest.main()