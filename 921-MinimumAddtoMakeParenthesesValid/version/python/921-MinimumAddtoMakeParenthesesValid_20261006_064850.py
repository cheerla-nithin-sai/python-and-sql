# Last updated: 10/6/2026, 6:48:50 AM
1class Solution:
2    def minAddToMakeValid(self, s: str) -> int:
3        l=[]
4        for i in s:
5            if i=='(':
6                l.append(i)
7            else:
8                if l and l[-1]=='(':
9                    l.pop()
10                else:
11                    l.append(i)
12        return len(l)
13
14        