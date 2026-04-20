# Last updated: 4/20/2026, 1:24:42 PM
class Solution:
    def getLongestSubsequence(self, words: List[str], groups: List[int]) -> List[str]:
        l=[]
        last=-1
        for i in range(len(words)):
            if groups[i]!=last:
                l.append(words[i])
                last=groups[i]
        return l