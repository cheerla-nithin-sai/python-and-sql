# Last updated: 6/16/2026, 11:05:24 AM
1class Solution:
2    def longestPalindrome(self, s: str) -> int:
3        d={}
4        c=0
5        for i in s:
6            if i not in d:
7                d[i]=1
8            else:
9                d[i]+=1
10        k=False
11        for j in d.values():
12            if j%2==0:
13                c+=j
14            else:
15                c+=j-1
16                k=True
17        if k:
18            return c+1
19        else:
20            return c