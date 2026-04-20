# Last updated: 4/20/2026, 1:26:05 PM
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        if len(word1)!=len(word2):
            return False
        
        s1 = Counter(word1)
        s2 = Counter(word2)
        if s1.keys()==s2.keys() and sorted(s1.values())==sorted(s2.values()):
            return True
        return False