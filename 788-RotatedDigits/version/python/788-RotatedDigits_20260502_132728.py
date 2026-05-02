# Last updated: 5/2/2026, 1:27:28 PM
1class Solution:
2    def rotatedDigits(self, n: int) -> int:
3        c=0
4        for d in range(1,n+1):
5            d=str(d)
6            if '3' in d or '4' in d or '7' in d:
7                continue
8            if '2' in d or '5' in d or '6' in d or '9' in d:
9                c+=1
10        return c
11
12        