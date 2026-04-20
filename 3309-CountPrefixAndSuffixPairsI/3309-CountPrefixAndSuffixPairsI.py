# Last updated: 4/20/2026, 1:24:38 PM
class Solution:
    def isprefixandsuffix(self,s1,s2):
        self.s1=s1
        self.s2=s2
        return 1 if s2.startswith(s1) and s2.endswith(s1) else 0

    def countPrefixSuffixPairs(self, words: List[str]) -> int:
        c=0
        for i in range(len(words)):
            for j in range(i+1,len(words)):
                c+= self.isprefixandsuffix(words[i],words[j])
        return c


        