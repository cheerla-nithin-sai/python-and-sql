# Last updated: 6/16/2026, 10:41:12 AM
1class Solution:
2    def isPowerOfTwo(self, n: int) -> bool:
3        while n>0:
4            if n==1:
5                return True
6            if n%2!=0:
7                return False
8            n=n//2
9        return False