# Last updated: 4/21/2026, 8:31:59 AM
1class Solution:
2    def findSubstring(self, s: str, words: List[str]) -> List[int]:
3        l = sum(map(len,words))
4        k=[]
5        r=len(words[0])
6        n=len(s)
7        for i in range(n-l+1):
8            st=s[i:i+l]
9            if sorted([st[j:j+r] for j in range(0,len(st),r)])==sorted(words):
10                k.append(i)
11        return k