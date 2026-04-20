# Last updated: 4/20/2026, 1:26:26 PM
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        l=[]
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i!=j:
                    l.append(words[i])
        return list(set(l))
        