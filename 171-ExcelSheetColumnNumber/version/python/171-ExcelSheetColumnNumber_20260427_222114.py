# Last updated: 4/27/2026, 10:21:14 PM
1class Solution:
2    def titleToNumber(self, columnTitle: str) -> int:
3        c=0
4        for i in columnTitle:
5            c=c*26+(ord(i)-ord('A')+1)
6        return c 
7        