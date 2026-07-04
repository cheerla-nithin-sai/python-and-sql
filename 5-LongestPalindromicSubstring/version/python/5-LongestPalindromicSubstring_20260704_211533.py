# Last updated: 7/4/2026, 9:15:33 PM
1class Solution:
2    def longestPalindrome(self, s: str) -> str:
3        if len(s)<2:
4            return s
5        l=[]
6        for i in range(len(s)):
7            for j in range(i,len(s)+1):
8                k=s[i:j]
9                if len(k)>=1 and k[::-1]==k:
10                    l.append(k)
11        l.sort(key=len)
12        return l[-1]
13        