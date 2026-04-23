# Last updated: 4/23/2026, 7:25:08 AM
class Solution:
    def twoEditWords(self, queries: List[str], dictionary: List[str]) -> List[str]:
        l=[]
        for word in queries:
            for match in dictionary:
                d=0
                for j in range(len(word)):
                    if word[j]!=match[j]:d+=1
                if d<=2:
                    l.append(word)
                    break
        return l


