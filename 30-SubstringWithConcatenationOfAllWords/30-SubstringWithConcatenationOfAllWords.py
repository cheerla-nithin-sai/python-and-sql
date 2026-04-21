# Last updated: 4/21/2026, 8:42:45 AM
from collections import Counter
class Solution:
    def findSubstring(self, s: str, words: List[str]) -> List[int]:
        l = sum(map(len,words))
        k=[]
        r=len(words[0])
        n=len(s)
        for i in range(n-l+1):
            st=s[i:i+l]
            if Counter([st[j:j+r] for j in range(0,len(st),r)])==Counter(words):
                k.append(i)
        return k