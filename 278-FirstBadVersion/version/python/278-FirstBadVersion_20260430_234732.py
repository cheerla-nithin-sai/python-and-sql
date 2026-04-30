# Last updated: 4/30/2026, 11:47:32 PM
1# The isBadVersion API is already defined for you.
2# def isBadVersion(version: int) -> bool:
3
4class Solution:
5    def firstBadVersion(self, n: int) -> int:
6        l,r=0,n
7        while l<r:
8            m=(l+r)//2
9            if isBadVersion(m):
10                r=m
11            else:
12                l=m+1
13        return l