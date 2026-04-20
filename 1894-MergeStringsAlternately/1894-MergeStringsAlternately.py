# Last updated: 4/20/2026, 1:25:46 PM
class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        k=[]
        for i in range(max(len(word1),len(word2))):
            if i<len(word1):
                k.append(word1[i])
            if i<len(word2):
                k.append(word2[i])
        return "".join(k)        